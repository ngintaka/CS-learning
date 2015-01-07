//
// breakout.c
//
// Computer Science 50
// Problem Set 4
//

// standard libraries
#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Stanford Portable Library
#include "gevents.h"
#include "gobjects.h"
#include "gwindow.h"

// height and width of game's window in pixels
#define HEIGHT 600
#define WIDTH 400

// height and width of paddle in pixels
#define PADHEIGHT 10
#define PADWIDTH 55
#define PADLOC (HEIGHT-60)

// number of rows of bricks
#define ROWS 5

// number of columns of bricks
#define COLS 10

// radius of ball in pixels
#define RADIUS 10

// lives
#define LIVES 3

// prototypes
void initBricks(GWindow window);
GOval initBall(GWindow window);
GRect initPaddle(GWindow window);
GLabel initScoreboard(GWindow window);
void updateScoreboard(GWindow window, GLabel label, int points);
GObject detectCollision(GWindow window, GOval ball);

int main(void)
{
    // seed pseudorandom number generator
    srand48(time(NULL));

    // instantiate window
    GWindow window = newGWindow(WIDTH, HEIGHT);

    // instantiate bricks
    initBricks(window);

    // instantiate ball, centered in middle of window
    GOval ball = initBall(window);

    // instantiate paddle, centered at bottom of window
    GRect paddle = initPaddle(window);

    // instantiate scoreboard, centered in middle of window, just above ball
    GLabel label = initScoreboard(window);

    // number of bricks initially
    int bricks = COLS * ROWS;

    // number of lives initially
    int lives = LIVES;

    // number of points initially
    int points = 0;

    // keep playing until game over
    
    //set up ball velocity prior to loop
    double Xvelocity = drand48()*4;
    double Yvelocity = 3.0;

    while (lives > 0 && bricks > 0)
    {
        // move circle along x-axis
        move(ball, Xvelocity, Yvelocity);

        // bounce off right edge of window
        if (getX(ball) + getWidth(ball) >= WIDTH)        
        {
            Xvelocity = -Xvelocity;
        }

        // bounce off left edge of window
        else if (getX(ball) <= 0)
        {
            Xvelocity = -Xvelocity;
        }

        //bounce off bottom edge of window
        else if (getY(ball) >= HEIGHT)
        {
            lives--;
            removeGWindow(window, ball);
            if (lives)
            {
                ball = initBall(window);
                waitForClick();
            }      
        }
        
        //bounce off top edge of window
        else if (getY(ball) <= 0)
        {
            Yvelocity = -Yvelocity;
        }


        // linger before moving again
        pause(10);
        
        
        // check for mouse event
        GEvent event = getNextEvent(MOUSE_EVENT);

        // if we heard one
        if (event != NULL)
        {
            // if the event was movement
            if (getEventType(event) == MOUSE_MOVED)
            {
                // ensure paddle follows cursor
                double x = getX(event) - getWidth(paddle)/2;
                double y = PADLOC;
                if (x <= 0)  x = 0;
                else if (x + getWidth(paddle) >= WIDTH) x = WIDTH - getWidth(paddle);
                setLocation(paddle, x, y);
            }
        }

        GObject object = detectCollision(window, ball);
        
        if (object != NULL)
        {
            if (object == paddle)
            {
            Yvelocity = -Yvelocity;
            }

            else if (strcmp(getType(object), "GRect") == 0)
            {
                points++;
                removeGWindow(window, object);
                Yvelocity = -Yvelocity;      
            }
        }
       updateScoreboard(window, label, points); 
    }

    // wait for click before exiting
    waitForClick();

    // game over
    closeGWindow(window);
    return 0;
}

/**
 * Initializes window with a grid of bricks.
 */
void initBricks(GWindow window)
{
    int a = 2;
    int w = 35;
    int h = 10;
    int spacer = 5;
    string color = "RED";
    
        
    for (int r = 0; r < COLS; r++)   
        { 
        
        int b = 50; //reset to this height after each loop
        for (int c = 0; c < ROWS; c++)        
            {
            if (c == 0)
                color = "RED";
            if (c == 1)
                color = "ORANGE";
            if (c == 2)
                color = "YELLOW";
            if (c == 3)
                color = "GREEN";
            if (c == 4)
                color = "CYAN";   
            GRect brick = newGRect(a, b, w, h);
            setFilled(brick, true);
            setColor(brick, (color));
            add(window, brick);
            b = b + h + spacer; //draw columns         
            }     
        a = a + w + spacer; //move across to next column
        }
}

/**
 * Instantiates ball in center of window.  Returns ball.
 */
GOval initBall(GWindow window)
{

    GOval ball = newGOval(WIDTH/2 - RADIUS, HEIGHT/2 - RADIUS, RADIUS * 2, RADIUS * 2);
    setFilled(ball, true);
    setColor(ball, "MAGENTA");
    add(window, ball);
    return ball;
}

/**
 * Instantiates paddle in bottom-middle of window.
 */
GRect initPaddle(GWindow window)
{
    GRect paddle = newGRect(WIDTH/2-PADWIDTH/2, PADLOC, PADWIDTH, PADHEIGHT);
    setFilled(paddle, true);
    setColor(paddle, "BLACK");
    add(window, paddle);
    return paddle;  
}

/**
 * Instantiates, configures, and returns label for scoreboard.
 */
GLabel initScoreboard(GWindow window)
{
    GLabel label = newGLabel("TEST");
    setFont(label, "SansSerif-48");
    setColor(label, "LIGHT_GRAY");
    add(window, label);
    return label;
}

/**
 * Updates scoreboard's label, keeping it centered in window.
 */
void updateScoreboard(GWindow window, GLabel label, int points)
{
    // update label
    char s[12];
    sprintf(s, "%i", points);
    setLabel(label, s);

    // center label in window
    double x = (getWidth(window) - getWidth(label)) / 2;
    double y = (getHeight(window) - getHeight(label)) / 2;
    setLocation(label, x, y);
}

/**
 * Detects whether ball has collided with some object in window
 * by checking the four corners of its bounding box (which are
 * outside the ball's GOval, and so the ball can't collide with
 * itself).  Returns object if so, else NULL.
 */
GObject detectCollision(GWindow window, GOval ball)
{
    // ball's location
    double x = getX(ball);
    double y = getY(ball);

    // for checking for collisions
    GObject object;

    // check for collision at ball's top-left corner
    object = getGObjectAt(window, x, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's top-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-left corner
    object = getGObjectAt(window, x, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    // no collision
    return NULL;
}

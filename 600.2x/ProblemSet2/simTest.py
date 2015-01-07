import * from ps2.py

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    room = RectangularRoom(width, height)
    bot = robot_type(room, speed)
    count = 1 - num_robots
    total = 0
    for n in range(num_trials):        
        while room.getNumCleanedTiles() < (room.getNumTiles() * min_coverage):                 
            for r in range(num_robots): 
                bot.updatePositionAndClean()
                count += 1
        total = float(total + count)
    print total / num_trials / num_robots

runSimulation(1, 1.0, 5, 100, 5, 1, StandardRobot)
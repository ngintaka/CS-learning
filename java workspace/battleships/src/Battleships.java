import java.util.*;

public class Battleships{

	private UserInput askGuess = new UserInput();
	private ShipPosition shipPosition = new ShipPosition();
	private ArrayList<Ship> fleet = new ArrayList<Ship>();
	private int numGuesses = 0;
	
	public void setupGame(){
		Ship cruiser = new Ship();
		cruiser.setName("cruiser");
		Ship carrier = new Ship();
		carrier.setName("aircraft carrier");
		Ship battleship = new Ship();
		battleship.setName("battleship");
		
		fleet.add(cruiser);
		fleet.add(carrier);
		fleet.add(battleship);
		
		System.out.println("\nWelcome. Your goal is to sink three ships.");
		System.out.println("\nThere's a cruiser, an aircraft carrier and a battleship.");
		System.out.println("\nTry to sink them all in the fewest possible guesses!\n");
		
		for (Ship shipToPlace : fleet) {
			ArrayList<String> newLocation = shipPosition.placeShip(3);
			shipToPlace.setLocationCells(newLocation);
		}
	}
	
	public void playGame(){
		while (!fleet.isEmpty()) {
			String guess = askGuess.getUserInput("\nEnter a guess");
			checkGuess(guess);
		}
		endGame();
	}
	
	public void checkGuess(String guess) {
		numGuesses++;
		String result = "miss!";
		
		for(Ship shipToTest : fleet) {
			result = shipToTest.checkYourself(guess);
			if (result.equals("hit!")) {
				break;
			}
			if (result.equals("kill!")) {
				System.out.println("\nYou sunk the " + shipToTest.getName() + "!!");
				fleet.remove(shipToTest);
				break;
			}
		}
		System.out.println("\nThat's a " + result);
	}
	
	public void endGame() {
		System.out.println("\nYou've sunk all three ships!");
		if (numGuesses < 18) {
			System.out.println("It only took you " + numGuesses + " guesses");
			System.out.println("That's a pretty good result!");
		} else {
			System.out.println("You certainly took long enough to find then all!");
			System.out.println("It took you " + numGuesses + " guesses. Better luck next time.");
		}
	}
	
	public static void main(String[] args){
	Battleships game = new Battleships();
	game.setupGame();
	game.playGame();
	}
}
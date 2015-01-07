package Animals;

public class Dog implements Species {
	
	String name;
	int legs;
	
	Dog(String dogName, int numLegs) {
		name = dogName;
		legs = numLegs;
		System.out.println("\nHi! My name is " + name);
		
	}
	
	public void speciesName(String s){
		System.out.println("My breed is: " + s);
	}	
	
	public void makeSound(String s, int times){
		System.out.print("I say:");
		for (int i = 0; i< times; i++){
			System.out.print(" " + s);
		}
		System.out.println(".\n");
	}
	public static void main(String[] args) {
		int legs = Integer.parseInt(args[1]);
		Terrier dog1 = new Terrier(args[0], legs);
		System.out.println("I have " + dog1.legs + " legs.");
		dog1.speciesName("bulldog");
		dog1.makeSound("woof", 4);
			
	}
	
}
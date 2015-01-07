import java.util.*;

class Animal {
	String sound;
	
	Animal(){
		System.out.println("\nThere's a new Animal in town:");
	}
	
	String speak() {
		return sound;
	}
}

class Mammal extends Animal {
	final static int legs = 4;
	final static String bloodTemp = "warm";	
}

class Dog extends Mammal {
	public Dog() {
		sound = "woof";
	}
}

class Zoo {
	ArrayList zoo = new ArrayList();
	
}


class TestAnimal {
	public static void main(String[] args) {		
		Dog fido = new Dog();
		//Zoo animalZoo = new Zoo();
		//animalZoo.zoo.add(fido);
		String voice = fido.speak();
		System.out.println("\nHi, my name is fido. I have " + fido.legs + " legs and when I speak I say \""
			+ voice + "\"! My blood is " + fido.bloodTemp + ".\n");
		}
	}
}
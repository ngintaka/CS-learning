public class ArgsTest {
	
	public static void main(String[] args) {
		int length = args.length;
		System.out.println("\nThere are " + length + " arguments\n");
		for (int i : args) {
			System.out.println(args[i]);
			}	
	}
}
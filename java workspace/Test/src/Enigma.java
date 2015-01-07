
public class Enigma {
	
	public static void enigma(int x) {
		if (x == 0) {
		return;
		} else {
		enigma(x/2);
		}
		System.out.print(x%2);
		}

}

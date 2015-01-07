public class TimesTable {

public static void main(String[] args) {

	int multiplier = Integer.parseInt(args[0]);

	for (int x = 1; x < 15; x++)
		System.out.println(x + " times " + multiplier + " is " + (x * multiplier));

}


}
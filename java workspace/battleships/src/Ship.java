import java.util.*;

public class Ship {
	
	private ArrayList<String> locationCells;
	private String name;
	
	public void setLocationCells(ArrayList<String> cells){
		locationCells = cells;
	}
	
	public void setName(String n) {
		name = n;
	}
	
	public String getName() {
		return name;
	}
	
	
	public String checkYourself(String guess) {
		String result = "miss!";
		int index = locationCells.indexOf(guess);
		if (index >= 0) {
			locationCells.remove(index);
			
			if (locationCells.isEmpty()) {
				result = "kill!";
			} else {
				result = "hit!";
			}	
		}
		return result;
	}
}
import java.awt.*;
import java.util.*;
import javax.swing.*;

class Curse {
	String curse;
	
	Curse(String[]... args){
		ArrayList<String> words = new ArrayList<String>();
		for (String[] arg : args) {
			words.add(randomWord(arg));
		}
		int listsLen = words.size();
		
		curse = "\nYou are a ";
		for (int i = 0; i < (listsLen-1); i++){
			curse = curse + words.get(i) +", ";
		}	
		curse = curse + words.get(listsLen-1) + "!";
	}
	
	public String getCurse(){
		return curse;
	}
	
	private String randomWord(String[] wordList) {
		String wrd = wordList[(int)(Math.random() * wordList.length)];
		return wrd;
	}
}
public class CurseMaker {
	private void printCurses(int n, String[] adj1List, String[] adj2List, String[] nounList){
				for (int i = 0; i < n; i++) {
					Curse curse = new Curse(adj1List, adj2List, nounList);
					System.out.println(curse.getCurse());
				}
	}
	
	private void guiCurse(String[] adj1List, String[] adj2List, String[] nounList) {
			Curse guiCurse = new Curse(adj1List, adj2List, nounList);
			String output = guiCurse.getCurse();
			JFrame frame = new JFrame("Curse of the Day");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.pack();
			frame.setSize(300,300);
			frame.setLocation(600,300);
			JLabel label = new JLabel(output,JLabel.CENTER);
			frame.add(label);
			frame.setVisible(true);
	}
	
	public static void main(String[] args) {
		String[] adj1List = {"big", "fat", "cold", "ridiculous", "tiny", "weak", "desperate", "smelly", "baldy", "slippery"};
		String[] adj2List = {"hairy", "clammy", "angry", "green", "snotty", "monkey-like", "rancid", "snotty"};
		String[] nounList = {"pig", "dog", "hobbit", "piece of trash", "lazybones", "sandwich", "clod", "armpit", "frankenstein", "monster", "trashbag", "doofus"};
		
		int n = Integer.parseInt(args[0]);
		
		CurseMaker newCurse = new CurseMaker();
		if (n > 1) newCurse.printCurses(n, adj1List, adj2List, nounList);
		else newCurse.guiCurse(adj1List, adj2List, nounList);
	}
}
import java.io.*;

public class FileTest {
	
	File f = new File("testfile.txt");
	
	public static void main(String[] args) {
		
		String text = args[0];
		FileTest fileTest = new FileTest();
		fileTest.goWrite(text);
		fileTest.goRead();	
	}
	
	private void goWrite(String text) {
		try {
			FileWriter writer = new FileWriter(f, true);
			writer.write(text + "\n");
			writer.close();
		} catch(IOException e){e.printStackTrace();}		
	}
	
	private void goRead(){
		try {
			FileReader filereader = new FileReader(f);
			BufferedReader reader = new BufferedReader(filereader);
			
			String line = null;
			
			while ((line = reader.readLine()) != null) {
				System.out.println(line);
			}
			reader.close();
		}catch(Exception e) {e.printStackTrace();}
	}
}
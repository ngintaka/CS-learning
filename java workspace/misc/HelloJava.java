import java.awt.*;
import javax.swing.*;

class HelloComponent extends JComponent {
	public void paintComponent( Graphics g) {
		g.drawString("Hello Javaboy!", 125, 95);		
	}		
}

public class HelloJava {
	public static void main(String[] args) {
		JFrame frame = new JFrame("Hello Java");
		HelloComponent hello = new HelloComponent();
		frame.add(hello);
		frame.setSize(300,300);
		frame.setVisible(true);
		
	}

}
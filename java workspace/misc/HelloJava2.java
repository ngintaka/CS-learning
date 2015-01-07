import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class HelloJava2 {
	public static void main(String[] args) {
		JFrame frame = new JFrame("Hello Java2");
		HelloComponent2 newObj = new HelloComponent2(args[0]);
		frame.add(newObj);
		//frame.getContentPane().add(new HelloComponent2(args[0])); //alternative version
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300,300);
		frame.setVisible(true);	
	}
}

class HelloComponent2 extends JComponent
	implements MouseMotionListener {
		String theMessage;
		int messageX = 125, messageY = 95;
		
		public HelloComponent2( String message) {
			theMessage = message;
			addMouseMotionListener(this);			
		}
	
	public void paintComponent( Graphics g) {
		g.drawString(theMessage, messageX, messageY);		
	}		

	public void mouseDragged(MouseEvent e) {
		messageX = e.getX();
		messageY = e.getY();
		repaint();
		
	}

	public void mouseMoved(MouseEvent e) {}
}
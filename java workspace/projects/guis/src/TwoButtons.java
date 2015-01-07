import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TwoButtons {
	
	JFrame frame;
	JLabel label;
	int numClicks;
	
	public static void main(String[] args) {
		TwoButtons twoButts = new TwoButtons();
		twoButts.go();
	}
	
	public void go() {
		frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JButton button1 = new JButton("Change text");
		button1.addActionListener(new LabelListener());
			
		JButton button2 = new JButton("Change color");
		button2.addActionListener(new ButtonListener());
		
		label = new JLabel("Click counter");
		MyDrawPanel drawPanel = new MyDrawPanel();
		
		frame.getContentPane().add(BorderLayout.EAST, button1);
		frame.getContentPane().add(BorderLayout.SOUTH, button2);
		frame.getContentPane().add(BorderLayout.WEST, label);
		frame.getContentPane().add(BorderLayout.CENTER, drawPanel);
		
		frame.setSize(400,300);
		frame.setVisible(true);	
	}
	
	class LabelListener implements ActionListener {
		public void actionPerformed(ActionEvent event) {
			numClicks++;
			label.setText("NumClicks = " + numClicks);
		}
	}
	
	class ButtonListener implements ActionListener {
		public void actionPerformed(ActionEvent event){
		frame.repaint();
		}
	}
	
	class MyDrawPanel extends JPanel {
		
		public void paintComponent(Graphics g) {
		Graphics2D g2d = (Graphics2D) g;
		
		int red = (int) (Math.random() * 256);
		int blue = (int) (Math.random() * 256);
		int green = (int) (Math.random() * 256);
		Color startColor = new Color(red, green, blue);
		
		red = (int) (Math.random() * 256);
		blue = (int) (Math.random() * 256);
		green = (int) (Math.random() * 256);
		Color endColor = new Color(red, green, blue);
		
		
		GradientPaint gradient = new GradientPaint(70, 70, startColor, 100, 100, endColor);
		g2d.setPaint(gradient);
		g2d.fillOval(70,70,100,100);
		}
	}
}
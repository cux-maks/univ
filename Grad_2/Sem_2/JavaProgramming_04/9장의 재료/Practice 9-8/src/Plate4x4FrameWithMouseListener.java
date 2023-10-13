import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Plate4x4FrameWithMouseListener extends JFrame {
	public Plate4x4FrameWithMouseListener() {
		super("3x4 Color Frame");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new GridLayout(4, 3));
		
		JLabel [] label = new JLabel [12];
		for(int i=0; i<label.length; i++) {
			label[i] = new JLabel(Integer.toString(i));
			label[i].setOpaque(true);
			label[i].setBackground(Color.WHITE);			
			c.add(label[i]);
			
			label[i].addMouseListener(new MouseAdapter() {

				@Override
				public void mousePressed(MouseEvent e) {
					JLabel label = (JLabel)e.getSource();
					int r = (int)(Math.random()*256); // 0~255 사이의 red 성분
					int g = (int)(Math.random()*256); // 0~255 사이의 green 성분
					int b = (int)(Math.random()*256); // 0~255 사이의 blue 성분					
					label.setBackground(new Color(r, g, b));					
				}
				
			});
		}
		setSize(270,200);
		setVisible(true);
	}
	public static void main(String[] args) {
		new Plate4x4FrameWithMouseListener();
	}

}

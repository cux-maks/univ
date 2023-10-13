import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class MouseDraggingFrame extends JFrame {
	public MouseDraggingFrame() {
		super("드래깅동안 YELLOW로 변경");	
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setBackground(Color.GREEN);
		
		MyMouseListener ml = new MyMouseListener();
		c.addMouseMotionListener(ml);
		c.addMouseListener(ml);
		
		setSize(250,150);
		setVisible(true);
	}
	
	class MyMouseListener extends MouseAdapter implements MouseMotionListener {
		public void mouseDragged(MouseEvent e) {
			Container c = (Container)e.getSource();
			c.setBackground(Color.YELLOW);
		}
		
		public void mouseMoved(MouseEvent e) {}
		
		public void mouseReleased(MouseEvent e) {
			Container c = (Container)e.getSource();
			c.setBackground(Color.GREEN);
		}		
	}
	static public void main(String [] args) {
		new MouseDraggingFrame();
	}
}

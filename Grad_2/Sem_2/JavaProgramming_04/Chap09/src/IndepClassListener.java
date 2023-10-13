import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class IndepClassListener extends JFrame {
	
	public IndepClassListener() {
		
		setTitle("Action 이벤트 리스너 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		
		JButton btn = new JButton("Action");
		btn.addActionListener(new MyActionListener()); 
		c.add(btn);
		
		setSize(250, 120);
		setVisible(true);
	}
	
	private class MyActionListener implements ActionListener {
		
		public void actionPerformed(ActionEvent e) {
			
			JButton b = (JButton)e.getSource();
			if(b.getText().equals("Action"))
				b.setText("액션");
			else
				b.setText("Action");
			// InnerClassListener나 JFrame의 멤버 호출 가능
			// setTitle(b.getText()); // 프레임 타이틀에 버튼문자열 출력
			
		}
		
	}
	
	public static void main(String [] args) {
		new IndepClassListener();
	}
	
}

// 독립된 클래스로 이벤트 리스너를 작성한다.
//class MyActionListener implements ActionListener {
//	
//	public void actionPerformed(ActionEvent e) {
//		JButton b = (JButton)e.getSource(); 
//		if(b.getText().equals("Action")) 
//			b.setText("액션"); 
//		else
//			b.setText("Action"); 
//	}
//	
//}
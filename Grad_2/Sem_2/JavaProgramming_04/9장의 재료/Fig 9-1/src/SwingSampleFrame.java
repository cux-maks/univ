import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

@SuppressWarnings("all") // 아래 코드에서 발생하는 모든 경고를 컴파일러에게 억제할 것을 지시 
public class SwingSampleFrame extends JFrame {
	public SwingSampleFrame() {
		setTitle("이벤트 기반 프로그래밍");
		createMenu();
		createToolBar();
		createSplitPane();
		setSize(500, 400);
		setVisible(true);
	}

	private void createMenu() {
		JMenuBar mb = new JMenuBar(); // 메뉴바 생성
		mb.add(new JMenu("File")); // 메뉴바에 메뉴를 붙임
		mb.add(new JMenu("Edit"));
		mb.add(new JMenu("Source"));
		mb.add(new JMenu("Project"));
		mb.add(new JMenu("Run"));

		this.setJMenuBar(mb); // 메뉴바를 프레임에 붙임
	}
	
	private void createToolBar() {
		JToolBar bar = new JToolBar("Kitae Menu"); // 툴바 생성
		bar.setBackground(Color.LIGHT_GRAY);
		
		// 툴바에 컴포넌트 삽입
		JButton newBtn = new JButton("New");
		newBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				//메시지 다이얼로그 출력하여 버튼 눌렀음을 알림
				JOptionPane.showMessageDialog(SwingSampleFrame.this, "new 버튼을 눌렀습니다.",
						"Message", JOptionPane.ERROR_MESSAGE);
			}		
		});
		bar.add(newBtn);
		
		
		
		bar.add(new JButton(new ImageIcon("images/open.jpg")));
		bar.addSeparator();
		bar.add(new JButton(new ImageIcon("images/save.jpg")));
		bar.add(new JLabel("search"));
		bar.add(new JTextField("text field"));
		JComboBox combo = new JComboBox();
		combo.addItem("Java");
		combo.addItem("C#");
		combo.addItem("C");
		combo.addItem("C++");
		bar.add(combo);
		
		getContentPane().add(bar, BorderLayout.NORTH); // 툴바를  
	}

	private void createSplitPane() {
		String [] fruits= {"apple", "banana", "kiwi", "mango", "pear", 
				"peach", "berry", "strawberry", "blackberry"};

		JList scrollList = new JList(fruits);
		JSplitPane pane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT,
				new JScrollPane(scrollList), new JScrollPane(new JLabel(new ImageIcon("images/img1.jpg")))); // JTabbedPane.LEFT
		getContentPane().add(pane, BorderLayout.CENTER);
	}

	public static void main(String[] args) {
		new SwingSampleFrame();
	}
}
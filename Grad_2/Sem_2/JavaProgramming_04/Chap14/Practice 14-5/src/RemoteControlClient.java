import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import javax.swing.*;

public class RemoteControlClient extends JFrame {
	private BufferedReader in = null;
	private BufferedWriter out = null;
	private ServerSocket listener = null;
	private Socket socket = null;

	private String [] btnText = { "LEFT", "RIGHT", "UP", "DOWN", "Connect" };	
	private JButton [] btns = { 
			new JButton(btnText[0]), 
			new JButton(btnText[1]), 
			new JButton(btnText[2]), 
			new JButton(btnText[3]),
			new JButton(btnText[4])
	};	
	
	public RemoteControlClient() {
		super("원격 제어 클라이언트");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new BorderLayout());
		c.add(btns[0], BorderLayout.WEST);
		c.add(btns[1], BorderLayout.EAST);
		c.add(btns[2], BorderLayout.NORTH);
		c.add(btns[3], BorderLayout.SOUTH);
		c.add(btns[4], BorderLayout.CENTER);		
		

		MyAction listener = new MyAction();
		for(int i=0; i<btns.length; i++) {
			btns[i].addActionListener(listener); // 모든 버튼에 리스너 등록
			btns[i].setEnabled(false); 	// 연결될 때까지 모든 버튼 비활성화
		}
		
		btns[4].setEnabled(true); // 연결 버튼만 활성화
		
		setSize(100, 150);
		setVisible(true);
	}
	
	private void setupConnection() throws IOException {
		socket = new Socket("localhost", 9999); // 클라이언트 소켓 생성. 연결 시도
		setTitle("연결됨");
		
		// 모든 버튼 활성화
		for(int i=0; i<btns.length; i++) btns[i].setEnabled(true);
		
		btns[4].setEnabled(false); // 연결 버튼만 비활성화
		
		in = new BufferedReader(new InputStreamReader(socket.getInputStream())); // 클라이언트로부터의 입력 스트림
		out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())); // 클라이언트로의 출력 스트림
	}
	
	private static void handleError(String string) {
		System.out.println(string);
		System.exit(1);
	}
	
	class MyAction implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent e) {
			try {
				JButton b = (JButton)e.getSource();
				String msg=""; 
				if(b == btns[0]) msg = btnText[0]; // left button
				else if(b == btns[1]) msg = btnText[1]; // right button			
				else if(b == btns[2]) msg = btnText[2]; // up button
				else if(b == btns[3]) msg = btnText[3]; // down button
				else if(b == btns[4]) { // Connect 버튼의 경우
					try {
						setupConnection();
						return;
					} catch (IOException e1) {
						handleError(e1.getMessage());
					}			
				}
				
				// 방향 지시 메시지 전송
				out.write(msg+"\n");
				out.flush();
			} catch (IOException e1) {
				handleError(e1.getMessage());
			} 			
		}		
	}

	
	public static void main(String[] args) {
		new RemoteControlClient();
	}

}

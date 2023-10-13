import java.awt.*;
import java.io.*;
import java.net.*;
import javax.swing.*;

public class RemoteControlServer extends JFrame {
	private BufferedReader in = null;
	private BufferedWriter out = null;
	private ServerSocket listener = null;
	private Socket socket = null;
	
	private JLabel label = new JLabel("Java");
	
	public RemoteControlServer() {
		super("원격 서버");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(null); // 배치관리자 삭제
		label.setSize(100, 30);
		label.setEnabled(false);
		label.setLocation(10, 10);
		label.setFont(new Font("Consolas", Font.ITALIC, 30));
		label.setForeground(Color.MAGENTA);
		c.add(label);
		
		setSize(250, 250);
		setVisible(true);
		
		try {
			setupConnection();
		} catch (IOException e) {
			handleError(e.getMessage());
		}
	}
	
	private void setupConnection() throws IOException {
		listener = new ServerSocket(9999); // 서버 소켓 생성
		
		 // 클라이언트로부터 연결 요청 대기
		socket = listener.accept();

		// 클라이언트가 연결되면 레이블을 활성화 시킴
		label.setEnabled(true); // 연결을 나타내는 표시
		in = new BufferedReader(new InputStreamReader(socket.getInputStream())); // 클라이언트로부터의 입력 스트림
		out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())); // 클라이언트로의 출력 스트림
		
		// 원격 연결 서비스 스레드를 만들어 가동
		new StubThread().start();
	}
	
	private static void handleError(String string) {
		System.out.println(string);
		System.exit(1);
	}
	
	
	class StubThread extends Thread {
		@Override
		public void run() {
			String msg = null;
			while (true) {
				try {
					msg = in.readLine(); // 상대로부터 한 행의 문자열 받기
				} catch (IOException e) {
					handleError(e.getMessage());
				}
				
				// 현재 레이블의 위치
				int x = label.getX(); 
				int y = label.getY();
				
				switch(msg) {
					case "LEFT" :
						if(x-10 < 0) x = 0;  // 왼쪽으로 더 갈 수 없는 경우			
						label.setLocation(x-10, y); 
						break;
					case "RIGHT" :
						if(x+10 > label.getParent().getWidth()) 
							break; // 오른쪽으로 더 갈 수 없는 경우 그냥 리턴			
						label.setLocation(x+10, y); 
						break;				
					case "UP" :
						if(y-10 < 0) y = 0; // 위쪽으로 더 갈 수 없는 경우
						label.setLocation(x, y-10); 
						break;
					case "DOWN" :
						if(y+10 > label.getParent().getHeight()) 
							break; // 아래쪽으로 더 갈 수 없는 경우 그냥 리턴
						label.setLocation(x, y+10); 
						break;
					default : // 클라이언트로부터 잘못된 지시. 어떻게 처리할까? 현재는 아무 반응없이 넘어간다.
				}
				
				label.getParent().repaint(); // 레이블의 부모 컨테이너부터 다시 그리기(레이블 자신 다시 그려짐)
			}
		}	
	}
	
	public static void main(String[] args) {
		new RemoteControlServer();
	}

}

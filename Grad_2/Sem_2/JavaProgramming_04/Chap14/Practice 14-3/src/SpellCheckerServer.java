import java.io.*;
import java.net.*;
import java.util.*;

public class SpellCheckerServer {
	private SpellChecker spellChecker;
	
	public SpellCheckerServer() { }
	
	public void run() {
		System.out.println("스펠체크 서버입니다.");
		spellChecker = new SpellChecker("words.txt");
		if(spellChecker.isFileRead()) { // 단어 파일이 읽혀졌을 경우 서비스 시작
			System.out.println("words.txt 읽기 완료");
			new ServerThread().start(); // 서비스 시작
		}
	}

	class ServerThread extends Thread { // 클라이언트의 접속을 받는 서버 스레드
		@Override
		public void run() {
			ServerSocket listener = null;
			Socket socket = null;
			try {
				listener = new ServerSocket(9998);
				while(true) {
					socket = listener.accept();
					System.out.println("클라이언트 연결됨");
					new ServiceThread(socket).start(); // 접속한 클라이언트를 전담하여 서비스하는 스레드 생성
				}
				
			} catch (IOException e) {
				e.printStackTrace();
			}
			
			try {
				if(listener != null)
					listener.close();
				if(socket != null)
					socket.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	class SpellChecker {
		private Vector<String> v = new Vector<String>(); // 파일로부터 읽은 단어를 저장하는 벡터
		private boolean fileOn = false;
		
		public SpellChecker(String fileName) {
			try {
				Scanner reader = new Scanner(new FileReader(fileName)); // 파일을 읽기 위한  scanner
				while(reader.hasNext()) {
					String word = reader.nextLine(); // 라인 단위로 단어 파일 읽기
					v.add(word); // 읽은 단어를 벡터에 저장
				}
				reader.close();
				fileOn = true;
			} catch (FileNotFoundException e) {
				e.printStackTrace();
				fileOn = false;
			}
		}
		
		public boolean isFileRead() {
			return fileOn;
		}
		
		public boolean check(String word) { // word가 벡터 v에 있으면 true 리턴
			if(v.contains(word))
				return true;
			else
				return false;
		}
	}
	
	// 각 클라이언트를 전담하여 단어를 수신하고 "YES"나 "NO"를 전송하는 스레드
	class ServiceThread extends Thread {
		private Socket socket = null;
		private BufferedReader in = null;
		private BufferedWriter out = null;
		public ServiceThread(Socket socket) { // 클라이언트와 통신할 소켓을 전달받음
			this.socket = socket;
			try {
				in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
				out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		@Override
		public void run() {
			while(true) {
				try {
					String word = in.readLine(); // 단어 숫신
					boolean res = spellChecker.check(word); // 스펠이 정확한지 검사
					if(res == true) {
						out.write("YES\n");
						System.out.println("요청단어 " + word + "=YES");
					}
					else { 
						out.write("NO\n");
						System.out.println("요청단어 " + word + "=NO");						
					}
					out.flush();
				} catch (IOException e) {
					System.out.println("클라이언트 연결 종료");
					try {
						socket.close();
					} catch (IOException e1) {
						e1.printStackTrace();
					}
					return; // 스레드 종료
				}

			}
		}
	}
	
	public static void main(String[] args) {
		SpellCheckerServer checker = new SpellCheckerServer();
		checker.run();

	}

}

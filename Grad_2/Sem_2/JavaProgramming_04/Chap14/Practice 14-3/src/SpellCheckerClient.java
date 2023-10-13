import java.io.*;
import java.net.*;
import java.util.Scanner;

public class SpellCheckerClient {
	private Socket socket = null;
	private BufferedReader in = null;
	private BufferedWriter out = null;
	
	public SpellCheckerClient() { }
	
	public void run() {
		System.out.println("스펠체크 클라이언트입니다.");
		setupConnection();
		System.out.println("스펠체크 서버에 접속하였습니다.");		
		
		Scanner scanner = new Scanner(System.in);
		String word;
		while(true) {
			try {
				System.out.print("단어 >> ");
				word = scanner.next(); // 단어 읽기		
				if(word.equals("그만")) {
					System.out.println("프로그램을 종료합니다...");
					break;
				}
				out.write(word + "\n");
				out.flush();
					
				String result = in.readLine();
				System.out.println(result);
			} catch (IOException e1) {
				System.out.println("서버로부터 연결이 종료되었습니다...");
				break;
			}
		}
		scanner.close();
	}
	
	public void setupConnection() {
		try {
			socket = new Socket("localhost", 9998);
			in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		SpellCheckerClient checkerClient = new SpellCheckerClient();
		checkerClient.run();
	}

}

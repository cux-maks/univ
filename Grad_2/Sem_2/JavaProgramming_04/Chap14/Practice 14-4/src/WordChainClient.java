import java.io.*;
import java.net.*;
import java.util.Scanner;

public class WordChainClient {
	private Socket socket = null;
	private BufferedReader in = null;
	private BufferedWriter out = null;
	
	public WordChainClient() { }
	
	public void run() {
		System.out.println("끝말잇기  클라이언트입니다.");
		setupConnection();
		System.out.println("끝말잇기 게임 서버에 접속하였습니다.");		
		
		Scanner scanner = new Scanner(System.in);

		try {
			while(true) {
				String serverWord = in.readLine(); // 서버로부터 단어 수신
				if(serverWord.equals("win")) {
					System.out.print("클라이언트가 이겼습니다.");
					break;
				}

				System.out.println("서버>> " + serverWord);
				System.out.print("클라이언트>> ");
				String clientWord = scanner.next(); // 단어 읽기		
				if(clientWord.equals("그만")) {
					System.out.println("프로그램을 종료합니다...");
					break;
				}
				out.write(clientWord + "\n");
				out.flush();
					
				String result = in.readLine();
				if(result.equals("YES"))
					continue;
				else {
					System.out.print("클라이언트가 졌습니다.");
					break;
				}
			}
		} catch (IOException e1) {
			System.out.println("서버로부터 연결이 종료되었습니다...");
		}
		scanner.close();
	}
	
	public void setupConnection() {
		try {
			socket = new Socket("localhost", 9998);
			in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
		} catch (UnknownHostException e) {
			System.out.println("서버의 주소가 잘못되었습니다...");
			System.exit(0);
		} catch (IOException e) {
			System.out.println("서버가 꺼저 있는 등으로 서버에 연결할 수 없습니다...");
			System.exit(0);
		}
	}
	
	public static void main(String[] args) {
		WordChainClient checkerClient = new WordChainClient();
		checkerClient.run();
	}

}

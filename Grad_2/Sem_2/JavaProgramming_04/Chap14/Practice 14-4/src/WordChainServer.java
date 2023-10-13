import java.io.*;
import java.net.*;
import java.util.*;

public class WordChainServer {
	private SpellChecker spellChecker;
	private BufferedReader in = null;
	private BufferedWriter out = null;
	ServerSocket listener = null;
	Socket socket = null;
	
	public WordChainServer() { }
	
	public void run() {
		System.out.println("끝말잇기 서버입니다.");
		spellChecker = new SpellChecker("hangulwords.txt");
		spellChecker.isFileRead();
		System.out.println("hangulwords.txt 읽기 완료");

		try {
			listener = new ServerSocket(9998);
			socket = listener.accept();
			System.out.println("클라이언트 연결됨");	
			
			in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
			
			String startWord = spellChecker.selectWord(); // 시작 단어 선택
			System.out.println("시작 단어는 " + startWord + "입니다.");
			
			Scanner scanner = new Scanner(System.in);

			// 시작 단어를 보낸다.
			out.write(startWord + "\n");
			out.flush();
			
			// 화면에 단어를 출력한다.
			System.out.println("서버>> " + startWord);
			
			while(true) {
				// 상대로부터 단어를 받는다.
				String clientWord = in.readLine(); // 단어 숫신

				// 상대가 보내온 단어를 화면에 출력한다.
				System.out.println("클라이언트>> " + clientWord);
				
				boolean res = spellChecker.check(clientWord); // 스펠이 정확한지 검사
				if(res == true) { // 상대편 성공
					out.write("YES\n");
					out.flush();
				}
				else { // 상대편이 졌습니다. 
					out.write("NO\n");
					out.flush();
					System.out.println("서버가 이겼습니다.");
					break; // I win!!
				}

				// 사용자로부터 단어를 읽는다.
				System.out.print("서버>> ");
				String serverWord = scanner.next();
		
				res = spellChecker.check(serverWord); // 스펠이 정확한지 검사
				
				if(res == true) { // 사용자 성공
					// 클라이언트로 단어를 보낸다.
					out.write(serverWord + "\n");
					out.flush();
					continue;
				}
				else // 서버가 졌습니다.!!
					// 클라이언트가 이겼음을 나타내는 단어를 보낸다.
					out.write("win\n"); // 상대가 이겼음을 보냄
					out.flush();
					System.out.println("서버가 졌습니다.");										
					break;
			}
			scanner.close();
			
		} catch (IOException e) {
			System.out.println("클라이언트 연결 종료");
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
	
	class SpellChecker {
		private String startWord=null;
		private String currentWord=null;
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
			// System.out.println(currentWord + ":" + word);
			
			if(v.contains(word)) { // word가 벡터에 들어 있는지 검사
				char lastChar = currentWord.charAt(currentWord.length()-1);
				char firstChar = word.charAt(0);
				if(lastChar == firstChar) { // word의 끝 글자와 현재 단어의 끝 글자가 같다면
					currentWord = word;
					return true;
				}
				else
					return false;
			}
			else
				return false;
		}
		
		public String selectWord() {
			int index = (int)(Math.random()*v.size()+1); // 전체 단어 중에서 하나 선택
			startWord = v.get(index);
			currentWord = startWord;
			return startWord;
		}
	}
	
	public static void main(String[] args) {
		WordChainServer checker = new WordChainServer();
		checker.run();

	}

}

// 이중 for 문

public class main {

	public static void main(String[] args) {
		
		for(int i = 1; i < 14; i++) {
			for(int j = 1; j < 10; j++) {
				System.out.println(i + "*" + j + "=" + i*j);
			}
		}
		
		for(int i = 1; i < 14; i++) {
			for(int j = 1; j < 10; j++) {
				System.out.print(i + "*" + j + "=" + i*j + "	");
			}
			System.out.println();
		}

	}

}

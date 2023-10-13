public class main {

	public static void main(String[] args) {
		
		for(int i = 1; i < 100; i++) {
			
			int a = i%10;
			int b = i/10;
			
			if(i >= 10 && a%3 == 0 && b%3 == 0 && a != 0) System.out.println(i + "박수두번");
			else if(i < 10 && a%3 == 0) System.out.println(i + "박수한번");
			else if(i >= 10 && a == 0 && b%3 == 0) System.out.println(i + "박수한번");
			else if(i >= 10 && a != 0 && (a%3 == 0 || b%3 == 0)) System.out.println(i + "박수한번");
				
		}
			
	}

}

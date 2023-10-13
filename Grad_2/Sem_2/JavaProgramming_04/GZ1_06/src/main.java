import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		int money = in.nextInt();
		in.close();
		int O_man = 0;
		int man = 0;
		int chun = 0;
		int O_back = 0;
		int back = 0;
		int ship = 0;
		int ill = 0;
		
		O_man = money >= 50000 ? money/50000 : 0;
		money -= O_man * 50000;
		man = money >= 10000 ? money/10000 : 0;
		money -= man * 10000;
		chun = money >= 1000 ? money/1000 : 0;
		money -= chun * 1000;
		O_back = money >= 500 ? money/500 : 0;
		money -= O_back * 500;
		back = money >= 100 ? money/100 : 0;
		money -= back * 100;
		ship = money >= 10 ? money/10 : 0;
		money -= ship * 10;
		ill = money >= 1 ? money/1 : 0;
		
		System.out.print("오만원 ");
		System.out.print(O_man);
		System.out.print("개, 만원 ");
		System.out.print(man);
		System.out.print("개, 천원 ");
		System.out.print(chun);
		System.out.print("개, 500원 ");
		System.out.print(O_back);
		System.out.print("개, 100원 ");
		System.out.print(back);
		System.out.print("개, 10원 ");
		System.out.print(ship);
		System.out.print("개, 1원" );
		System.out.print(ill);
		System.out.print("개");

	}

}

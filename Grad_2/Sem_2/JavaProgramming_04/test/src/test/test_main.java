package test;

class test_class_2 extends test_class {
	public test_class_2(int num) { super(num); }
	public void print_id() { super.print_id(); }
}

public class test_main {

	public static void main(String[] args) {
		test_class_2 tc2 = new test_class_2(123);
		tc2.print_id();

	}

}
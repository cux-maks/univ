import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class CalculatorFrame extends JFrame {
	private CenterPanel centerPanel = new CenterPanel();
	private NorthPanel northPanel = new NorthPanel();
	
	public CalculatorFrame() {
		super("간단한 계산기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane(); // 컨텐트팬은 디폴트로 BorderLayout 배치 관리자.
		
		c.add(centerPanel, BorderLayout.CENTER);
		c.add(northPanel, BorderLayout.NORTH);
		
		setSize(270,250);
		setVisible(true);
	}
	

	class CenterPanel extends JPanel {
		private JButton b [] = { new JButton("+"), new JButton("-"), new JButton("x"), new JButton("/") };
		private JButton ceBtn = new JButton("CE");
		private JButton calBtn = new JButton("계산");
		private boolean waitForNewCalc = true;  // 지나번 계산 후 첫입력을 기다리는 있으면 true
		
		public CenterPanel() {
			setBackground(Color.WHITE);
			setLayout(new GridLayout(4,4,5,5)); // GridLayout 배치관리자
			for(int i=0; i<10; i++) {
				JButton b = new JButton(Integer.toString(i));
				add(b);
				
				// 숫자 버튼이 눌러졌을 때 처리
				b.addActionListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						if(waitForNewCalc) {
							waitForNewCalc = false;
							northPanel.clear(); // 수식창 지우기
						}
						northPanel.attachExp(e.getActionCommand()); // e.getActionCommand()는 버튼 표면의 숫자 문자열	
					}					
				});
			}
			add(ceBtn);
			add(calBtn);

			for(int i=0; i<b.length; i++) {
				b[i].setBackground(Color.CYAN);
				add(b[i]);
				
				// 연산자 버튼이 눌러졌을 때 처리
				b[i].addActionListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						if(waitForNewCalc) {
							waitForNewCalc = false;
							northPanel.clear(); // 수식창 지우기
						}
						northPanel.attachExp(e.getActionCommand()); // e.getActionCommand()는 버튼 표면의 연산자 문자열	
					}					
				});
			}
			
			
			// CE 버튼이 눌러졌을 때 처리
			ceBtn.addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					northPanel.clear();
				}				
			});
			
			// 게산 버튼이 눌러졌을 때 처리
			calBtn.addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					northPanel.calculate();
					waitForNewCalc = true;
				}				
			});
		}
	}
	
	class NorthPanel extends JPanel {
		private JTextField exp = new JTextField(10);
		private JTextField res = new JTextField(8);
		
		public NorthPanel() {
			setBackground(Color.LIGHT_GRAY);
			setOpaque(true);
			setLayout(new FlowLayout()); // JPanel이 디폴트로 FlowLayout이지만, 확실히 하기 위해		
			add(new JLabel("수식"));
			add(exp);
			add(new JLabel("결과"));
			add(res);
		}
		
		public void clear() {
			exp.setText("");
			res.setText("");
		}
		
		public void calculate() {
			String text = exp.getText();
			StringTokenizer st = new StringTokenizer(text, "+-x/");
			if(st.countTokens() != 2) {
				exp.setText("잘못된 수식");
				return;				
			}

			int op1=0, op2=0;
			try {
				op1 = Integer.parseInt(st.nextToken()); // 첫번째 정수
				op2 = Integer.parseInt(st.nextToken()); // 두번재 정수
			} catch(NumberFormatException e) { // 예: 2*4-5의 경우
				exp.setText("잘못된 수식");
				return;
			}
			
			// 연산자 알아내기
			int index = text.indexOf(Integer.toString(op2)); // 두번째 숫자의 시작 위치 파악
			String operator = text.substring(index-1, index); // 두번째 숫자 바로 앞의 한 개의 문자열이 연산자임
			
			double r = 0; 
			switch(operator) {
				case "+" : r = op1 + op2; break;
				case "-" : r = op1 - op2; break;
				case "x" : r = op1 * op2; break;
				case "/" : 
					if(op2 == 0)  {
						exp.setText("0으로 나눌 수 없음");
						return;				
					}
					r = op1 / op2; 
					break;
			}
			
			res.setText(Double.toString(r)); // 계산 결과 출력
			
		}
		
		public void attachExp(String s) {
			String text = exp.getText();
			text += s;
			exp.setText(text);
		}
	}
	
	public static void main(String[] args) {
		new CalculatorFrame();
	}

}
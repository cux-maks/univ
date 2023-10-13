#include <Adafruit_LiquidCrystal.h>
#include <EEPROM.h>
// #include <Li
int COIN = 0;
int SIGNAL_LIGHT = 10;  //led 다이오드 핀 설정
int TOPSCORE = 0;
Adafruit_LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup() {
  // put your setup code here, to run once:
  pinMode(SIGNAL_LIGHT, OUTPUT);  //led다이오드 핀 설정
  lcd.begin(16, 2);
}

void loop() {
  /*

  readyToFingerFlick();
  finishFingerFlick();
  printHit();
  printCoin();
  printInsertCoin();
  printScore();
  printCurrentScore();
  printTopScore();
  
  */
}
//딱밤대기시 led다이오드에 점등 함수
void readyToFingerFlick() {
  if (COIN == 0) return;
  digitalWrite(SIGNAL_LIGHT, HIGH);
}
//딱밤때리면 led다이오드 소등 함수
void finishFingerFlick() {
  digitalWrite(SIGNAL_LIGHT, LOW);
}
//딱밤대시기 HIT!! 문자 출력 함수
void printHit() {
  lcd.clear();
  printTopScore();
  lcd.setCursor(5, 1);
  lcd.print("HIT!!");
}
//현재 코인 수 알려주는 함수
void printCoin() {
  lcd.clear();
  printTopScore();
  lcd.setCursor(5, 1);
  lcd.print(COIN);
  lcd.print("COIN!!");
}
void printInsertCoin() {
  lcd.clear();
  printTopScore();
  lcd.setCursor(1, 1);
  lcd.print("Insert COIN!!");
}
//lcd에 점수 출력 함수
void printScore(int currscore) {
  printCurrentScore(currscore);
  //최고 기록 경신 시 top스코어도 깜빡임
  if (currscore > TOPSCORE) {
    for (int i = 0; i < 10; i++) {
      lcd.clear();
      delay(100);
      printTopScore();
      delay(100);
    }
  } else printTopScore();
}
//lcd에 현재 점수 출력 함수
void printCurrentScore(int currscore) {
  //스코어가 0점부터 차례로 올라가는 기능
  for (int i = 0; i < currscore; ++i) {
    lcd.clear();
    lcd.setCursor(7, 1);
    lcd.print(i);
    delay(1);
  }
  //글자 깜빡이는 기능
  for (int i = 0; i < 10; i++) {
    lcd.clear();
    delay(100);
    lcd.setCursor(7, 1);
    lcd.print(currscore);
    delay(100);
  }
}
//lcd에 TOPSCORE 출력 함수
void printTopScore() {
  lcd.setCursor(7, 0);
  lcd.print(TOPSCORE);
}
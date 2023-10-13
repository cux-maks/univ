// 라이브러리
// lcd, led 제어 라이브러리
#include <LiquidCrystal.h>
#include <EEPROM.h>

// led_strip 제어 라이브러리
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

// bgm 제어 라이브러리

// oled_disp 제어 라이브러리
#include "U8glib.h"

// lcd, led 제어 변수
#define LCD_DISPLAY 10
int COIN = 0;
int SIGNAL_LIGHT = 31;  //led 다이오드 핀 설정
int TOPSCORE = 0;

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

// led_strip 제어 변수
#define PIN 30
#define NUMPIXELS 32
#define PIXEL_COUNT 32

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 100;

// bgm 제어 변수
#define speakerPin 23                                                               //부저 핀번호
#define numTones 13                                                                 //음계 숫자
int tones[] = { 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523 };  //음계 설정(도~도)

//BGM
#define NOTE_B0 31
#define NOTE_C1 33
#define NOTE_CS1 35
#define NOTE_D1 37
#define NOTE_DS1 39
#define NOTE_E1 41
#define NOTE_F1 44
#define NOTE_FS1 46
#define NOTE_G1 49
#define NOTE_GS1 52
#define NOTE_A1 55
#define NOTE_AS1 58
#define NOTE_B1 62
#define NOTE_C2 65
#define NOTE_CS2 69
#define NOTE_D2 73
#define NOTE_DS2 78
#define NOTE_E2 82
#define NOTE_F2 87
#define NOTE_FS2 93
#define NOTE_G2 98
#define NOTE_GS2 104
#define NOTE_A2 110
#define NOTE_AS2 117
#define NOTE_B2 123
#define NOTE_C3 131
#define NOTE_CS3 139
#define NOTE_D3 147
#define NOTE_DS3 156
#define NOTE_E3 165
#define NOTE_F3 175
#define NOTE_FS3 185
#define NOTE_G3 196
#define NOTE_GS3 208
#define NOTE_A3 220
#define NOTE_AS3 233
#define NOTE_B3 247
#define NOTE_C4 262
#define NOTE_CS4 277
#define NOTE_D4 294
#define NOTE_DS4 311
#define NOTE_E4 330
#define NOTE_F4 349
#define NOTE_FS4 370
#define NOTE_G4 392
#define NOTE_GS4 415
#define NOTE_A4 440
#define NOTE_AS4 466
#define NOTE_B4 494
#define NOTE_C5 523
#define NOTE_CS5 554
#define NOTE_D5 587
#define NOTE_DS5 622
#define NOTE_E5 659
#define NOTE_F5 698
#define NOTE_FS5 740
#define NOTE_G5 784
#define NOTE_GS5 831
#define NOTE_A5 880
#define NOTE_AS5 932
#define NOTE_B5 988
#define NOTE_C6 1047
#define NOTE_CS6 1109
#define NOTE_D6 1175
#define NOTE_DS6 1245
#define NOTE_E6 1319
#define NOTE_F6 1397
#define NOTE_FS6 1480
#define NOTE_G6 1568
#define NOTE_GS6 1661
#define NOTE_A6 1760
#define NOTE_AS6 1865
#define NOTE_B6 1976
#define NOTE_C7 2093
#define NOTE_CS7 2217
#define NOTE_D7 2349
#define NOTE_DS7 2489
#define NOTE_E7 2637
#define NOTE_F7 2794
#define NOTE_FS7 2960
#define NOTE_G7 3136
#define NOTE_GS7 3322
#define NOTE_A7 3520
#define NOTE_AS7 3729
#define NOTE_B7 3951
#define NOTE_C8 4186
#define NOTE_CS8 4435
#define NOTE_D8 4699
#define NOTE_DS8 4978


//Mario main theme melody
int melody[] = {
  NOTE_E7, NOTE_E7, 0, NOTE_E7,
  0, NOTE_C7, NOTE_E7, 0,
  NOTE_G7, 0, 0, 0,
  NOTE_G6, 0, 0, 0,

  NOTE_C7, 0, 0, NOTE_G6,
  0, 0, NOTE_E6, 0,
  0, NOTE_A6, 0, NOTE_B6,
  0, NOTE_AS6, NOTE_A6, 0,

  NOTE_G6, NOTE_E7, NOTE_G7,
  NOTE_A7, 0, NOTE_F7, NOTE_G7,
  0, NOTE_E7, 0, NOTE_C7,
  NOTE_D7, NOTE_B6, 0, 0,

  NOTE_C7, 0, 0, NOTE_G6,
  0, 0, NOTE_E6, 0,
  0, NOTE_A6, 0, NOTE_B6,
  0, NOTE_AS6, NOTE_A6, 0,

  NOTE_G6, NOTE_E7, NOTE_G7,
  NOTE_A7, 0, NOTE_F7, NOTE_G7,
  0, NOTE_E7, 0, NOTE_C7,
  NOTE_D7, NOTE_B6, 0, 0
};
//Mario main them tempo
int tempo[] = {
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,

  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,

  9,
  9,
  9,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,

  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,

  9,
  9,
  9,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
  12,
};

// oled_disp 제어 변수
U8GLIB_SSD1306_128X64 u8g(U8G_I2C_OPT_NONE);  // I2C / TWI

// fsr
int coinInput = A14;
int flickInput = A13;

void setup() {
  Serial.begin(9600);
  // lcd, led setup
  pinMode(SIGNAL_LIGHT, OUTPUT);  //led다이오드 핀 설정
  pinMode(LCD_DISPLAY, OUTPUT);
  digitalWrite(LCD_DISPLAY, HIGH);
  pinMode(12, OUTPUT);
  digitalWrite(12, LOW);
  pinMode(1, OUTPUT);
  digitalWrite(1, HIGH);

  lcd.begin(16, 2);

  TOPSCORE = EEPROM.read(0);

  // led_strip setup
#if defined(__AVR_ATtiny85__)
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  resetLed();
  pixels.begin();
  print_gameStart();

  //bgm 시작
  start();
  noTone(speakerPin);
  delay(500);
  bgm();

  // oled_disp setup

  // fsr setup

  randomSeed(analogRead(A15)); // 제출
}

void loop() {
  digitalWrite(SIGNAL_LIGHT, LOW);
  Serial.println("Start");
  // put your main code here, to run repeatedly:
  int currScore = 0;  // 현재 점수 0으로 초기화

  print_gameStart();  // 게임 시작 얼굴
  startled();         // led 시작
  resetLed();         // led 초기화
  printInsertCoin();  // 코인 입력 lcd 출력

  while (true) {               // 코인 입력 무한대기
    if (Coin_Sensor()) break;  // 입력시 break
  }
  coinSound();
  Serial.println("Coin inserted");
  digitalWrite(SIGNAL_LIGHT, HIGH);
  // readyToFingerFlick();  // 딱밤 대기 led 출력
  printHit();

  while (true) {                 // 딱밤 무한대기
    currScore = Flick_Sensor();  // 딱밤 센서 값 받아오기
    // delay(2000);
    if (currScore >= 7000) break;  // 최소 값 넘기면 중단
  }
  Serial.println("punch 전");

  hit();            // 타격 소리
  print_punched();  // 타격 얼굴
  delay(300);
  /*딱밤 치면 hit();
  delay(300);
  */
  
  Serial.print(currScore);
  Serial.print("  ");
  Serial.println(TOPSCORE);
  finishFingerFlick();            // 타격 종료 lcd 출력
  scoreled(currScore, TOPSCORE);  // led strip 출력
  printScore(currScore);          // 현재 점수 lcd 출력
  EEPROM.write(0, TOPSCORE);      // eeprom에 저장
}

// lcd, led func def
/*
lcd, led func list

  readyToFingerFlick();
  finishFingerFlick();
  printHit();
  printCoin();
  printInsertCoin();
  printScore();
  printCurrentScore();
  printTopScore();

*/
/*
led_strip func list

resetLed();
scoredled(int score, int highscore);
startled();
rainbow();
rainbowCycle(uint8_t wait);
Wheel(byte WheelPos);

*/
/*
bgm func list

buzz(int targetPin, long frequency, long length);
bgm();
hit();
newRecord();
start();

*/
/*
oled_disp func list

u8g_prepare();
disp_clear();
print_gameStart();
print_notBestScore();
print_punched();
print_bestScore();
*/
/*
fsr func list

Coin_Sensor();
Flick_Sensor();

*/
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
      // delay(100);
      printTopScore();
      // delay(100);
    }
  } else printTopScore();
}
//lcd에 현재 점수 출력 함수
void printCurrentScore(int currscore) {
  //스코어가 0점부터 차례로 올라가는 기능
  for (int i = 0; i < currscore; i += 100) {
    lcd.clear();
    lcd.setCursor(7, 1);
    lcd.print(i);
    // delay(1);
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

// led_strip func def

void resetLed() {
  Serial.println("reset...");
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
    pixels.show();
    delay(1);
  }
  Serial.println("end");
}

void scoreled(int score, int highscore) {
  uint16_t i, j;
  // score = map(score, 0, 32, 0, 32);
  int maxi = map(score, 0, 9999, 0, 32);
  if (score <= highscore) {  //기록
    for (int i = 0; i < maxi; i++) {
      pixels.setPixelColor(i, Wheel((i + j) & 255));
      pixels.show();
      tone(speakerPin, tones[i % 13], delayval);
      delay(delayval);
      //rainbow(20,100,1000);
      //delay(delayval);
    }
    print_notBestScore();
    newRecordFail();
  } else if (score > highscore) {  //최고기록
    TOPSCORE = score;
    for (int i = 0; i < maxi; i++) {
      pixels.setPixelColor(i, Wheel((i + j) & 255));
      //rainbow(20,1000,100);
      pixels.show();
      tone(speakerPin, tones[i % 13], delayval);
      delay(delayval);
      //delay(delayval);
    }
    print_bestScore();
    newRecord();
  }
}

void startled() {  //게임시작
  rainbowCycle(1);
  delay(delayval);
}

//=====================================led 구현 함수================================================

void rainbow(uint8_t wait, int score, int highscore) {
  uint16_t i, j;

  for (j = 0; j < 256; j++) {
    for (i = 0; i < strip.numPixels(); i++) {
      pixels.setPixelColor(i, Wheel((i + j) & 255));
    }
    pixels.show();
    delay(wait);
  }
}

void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for (j = 0; j < 256 * 5; j++) {  // 5 cycles of all colors on wheel
    for (i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if (WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if (WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}

// bgm func def

void coinSound(){
  tone(speakerPin, NOTE_C6);
  delay(100);
  tone(speakerPin, NOTE_E6);
  delay(100);
  tone(speakerPin, NOTE_G6);
  delay(100);
  noTone(speakerPin);
}

void buzz(int targetPin, long frequency, long length) {
  digitalWrite(13, HIGH);
  long delayValue = 1000000 / frequency / 2;  // calculate the delay value between transitions
  //// 1 second's worth of microseconds, divided by the frequency, then split in half since
  //// there are two phases to each cycle
  long numCycles = frequency * length / 1000;  // calculate the number of cycles for proper timing
  //// multiply frequency, which is really cycles per second, by the number of seconds to
  //// get the total number of cycles to produce
  for (long i = 0; i < numCycles; i++) {  // for the calculated length of time...
    digitalWrite(targetPin, HIGH);        // write the buzzer pin high to push out the diaphram
    delayMicroseconds(delayValue);        // wait for the calculated delay value
    digitalWrite(targetPin, LOW);         // write the buzzer pin low to pull back the diaphram
    delayMicroseconds(delayValue);        // wait again or the calculated delay value
  }
  digitalWrite(13, LOW);
}

void bgm() {
  int size = sizeof(melody) / sizeof(int);
  for (int thisNote = 0; thisNote < size; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / tempo[thisNote];

    buzz(speakerPin, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);

    // stop the tone playing:
    buzz(speakerPin, 0, noteDuration);
  }
}
//BGM 끝

void hit() {  //때렸을때 효과음
  tone(speakerPin, tones[4]);
  delay(500);
  noTone(speakerPin);
}
/*void hitSound(){
  for(int i=0;i<13;i++){
    tone(speakerPin, tones[i])
    delay(150);
  }*/

void newRecord() {
  tone(speakerPin, NOTE_G4);
  delay(100);
  tone(speakerPin, NOTE_C5);
  delay(100);
  tone(speakerPin, NOTE_E5);
  delay(100);
  tone(speakerPin, NOTE_G5);
  delay(100);
  tone(speakerPin, NOTE_C6);
  delay(100);
  tone(speakerPin, NOTE_E6);
  delay(100);
  tone(speakerPin, NOTE_G6);
  delay(300);
  tone(speakerPin, NOTE_E6);
  delay(300);
  tone(speakerPin, NOTE_GS4);
  delay(100);
  tone(speakerPin, NOTE_C5);
  delay(100);
  tone(speakerPin, NOTE_DS5);
  delay(100);
  tone(speakerPin, NOTE_GS5);
  delay(100);
  tone(speakerPin, NOTE_C6);
  delay(100);
  tone(speakerPin, NOTE_DS6);
  delay(100);
  tone(speakerPin, NOTE_GS6);
  delay(300);
  tone(speakerPin, NOTE_DS6);
  delay(300);
  tone(speakerPin, NOTE_AS4);
  delay(100);
  tone(speakerPin, NOTE_D5);
  delay(100);
  tone(speakerPin, NOTE_F5);
  delay(100);
  tone(speakerPin, NOTE_AS5);
  delay(100);
  tone(speakerPin, NOTE_D6);
  delay(100);
  tone(speakerPin, NOTE_F6);
  delay(100);
  tone(speakerPin, NOTE_AS6);
  delay(300);
  tone(speakerPin, NOTE_AS6);
  delay(100);
  tone(speakerPin, NOTE_AS6);
  delay(100);
  tone(speakerPin, NOTE_AS6);
  delay(100);
  tone(speakerPin, NOTE_C7);
  delay(300);
  noTone(speakerPin);
}

void newRecordFail() {
  tone(speakerPin, NOTE_C5);
  delay(350);
  tone(speakerPin, NOTE_G4);
  delay(350);
  tone(speakerPin, NOTE_E4);
  delay(350);
  tone(speakerPin, NOTE_A4);
  delay(175);
  tone(speakerPin, NOTE_B4);
  delay(175);
  tone(speakerPin, NOTE_A4);
  delay(175);
  tone(speakerPin, NOTE_GS4);
  delay(350);
  tone(speakerPin, NOTE_AS4);
  delay(175);
  tone(speakerPin, NOTE_GS4);
  delay(350);
  tone(speakerPin, NOTE_G4);
  delay(175);
  tone(speakerPin, NOTE_F4);
  delay(175);
  tone(speakerPin, NOTE_G4);
  delay(500);
  noTone(speakerPin);
}

void start() {  //시작 효과음
  tone(speakerPin, tones[0]);
  delay(200);
  tone(speakerPin, tones[4]);
  delay(200);
  tone(speakerPin, tones[7]);
  delay(200);
  tone(speakerPin, tones[12]);
  delay(200);
  tone(speakerPin, tones[7]);
  delay(200);
  tone(speakerPin, tones[4]);
  delay(200);
  tone(speakerPin, tones[0]);
  delay(200);
}

// oled_func def

void u8g_prepare(void) {
  u8g.setFont(u8g_font_6x10);
  u8g.setFontRefHeightExtendedText();
  u8g.setDefaultForegroundColor();
  u8g.setFontPosTop();
}

void disp_clear() {
  u8g.firstPage();
  u8g_prepare();
  u8g.setRGB(0, 0, 0);
  do {

    u8g.drawBox(0, 0, 128, 64);
  } while (u8g.nextPage());
}

void print_gameStart() {
  u8g.firstPage();
  u8g_prepare();
  do {
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(51, 28, 10);
    u8g.drawCircle(75, 28, 10);
    u8g.setRGB(0, 0, 0);
    u8g.drawBox(0, 24, 128, 64);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 43, 10);
    u8g.setRGB(0, 0, 0);
    u8g.drawBox(0, 33, 128, 10);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 32, 30);
  } while (u8g.nextPage());
}

void print_notBestScore() {
  u8g.firstPage();
  u8g_prepare();
  do {
    u8g.setRGB(255, 255, 255);
    u8g.drawLine(65, 28, 79, 20);
    u8g.drawLine(49, 20, 63, 28);
    u8g.setRGB(0, 0, 0);
    u8g.drawBox(0, 24, 128, 64);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 50, 10);
    u8g.setRGB(0, 0, 0);
    u8g.drawBox(0, 50, 128, 13);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 32, 30);
  } while (u8g.nextPage());
}

void print_punched() {
  u8g.firstPage();
  u8g_prepare();
  do {
    u8g.setRGB(255, 255, 255);
    u8g.drawLine(65, 20, 100, 28);
    u8g.drawLine(25, 28, 60, 20);
    u8g.setRGB(0, 0, 0);
    u8g.drawBox(0, 24, 128, 64);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 50, 10);
    u8g.setRGB(0, 0, 0);
    u8g.drawBox(0, 50, 128, 13);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 32, 30);
  } while (u8g.nextPage());
}

void print_bestScore() {
  u8g.firstPage();
  u8g_prepare();
  do {
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(51, 28, 10);
    u8g.drawCircle(75, 28, 10);
    u8g.setRGB(0, 0, 0);
    u8g.drawBox(0, 24, 128, 64);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 43, 10);
    u8g.setRGB(255, 255, 255);
    u8g.drawCircle(63, 32, 30);
  } while (u8g.nextPage());
}

// fsr func def

bool Coin_Sensor() {
  if (analogRead(coinInput) == 1023) return true;
  else return false;
}

int Flick_Sensor() {
  
  int cnt = 0;

  while (cnt < 3){
    Serial.print("wating");
    int r = analogRead(flickInput);
    Serial.println(r);
    if (r >= 1023){
      cnt += 1;
    }
  }

  Serial.println("done");
  int val = random(7000, 10000);

// int val = analogRead(flickInput);

  return val;
}

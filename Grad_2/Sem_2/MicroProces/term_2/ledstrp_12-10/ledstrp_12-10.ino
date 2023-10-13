//줄 led(진현우) - 점수올라갈때, 최고기록 경신 시 점멸, 게임 시작 시 점멸
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define PIN 7
#define NUMPIXELS 32
#define PIXEL_COUNT 16

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 100;

void setup() {
  Serial.begin(9600);
#if defined(__AVR_ATtiny85__)
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif

  resetLed();

  pixels.begin();  
}

void loop() {
  // Serial.println("startLed");
  // startled();
  // delay(1000);    
  // resetLed();   
  // delay(1000);       
  Serial.println("scored(100, 1000)");
  scoreled(100, 1000);                   //기록테스트
  delay(1000);    
  resetLed();   
  delay(1000);   
  Serial.println("scored(1000, 100)");
  scoreled(1000, 100);                   //최고기록테스트
  delay(1000);    
  resetLed();   
  delay(1000);
}

void resetLed(){
  Serial.println("reset...");
  for(int i = 0; i < NUMPIXELS; i++){
    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
    pixels.show();
    delay(1);
  }
  Serial.println("end");
}

void scoreled(int score, int highscore) {
  score = map(score, 0, 1000, 0, 32);
  if (score <= highscore) {                              //기록
    for (int i = 0; i < score; i++) {
      pixels.setPixelColor(i, pixels.Color(0, 1, 0)); 
      pixels.show();                                  
      delay(delayval);                                 
    }
  } else if (score > highscore) {                        //최고기록
    highscore = score;
    for (int i = 0; i < highscore; i++) {
      pixels.setPixelColor(i, pixels.Color(0, 1, 0));  
      rainbow(20);
      pixels.show();    
      delay(delayval);  
    }
  }
}

void startled() {  //게임시작
  rainbowCycle(20);
  delay(delayval);  
}

//=====================================led 구현 함수================================================

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}

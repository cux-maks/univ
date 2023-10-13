#include "U8glib.h"

U8GLIB_SSD1306_128X64 u8g(U8G_I2C_OPT_NONE);  // I2C / TWI

void u8g_prepare(void) {
  u8g.setFont(u8g_font_6x10);
  u8g.setFontRefHeightExtendedText();
  u8g.setDefaultForegroundColor();
  u8g.setFontPosTop();
}

void disp_clear(){
u8g.firstPage();
  u8g_prepare();
  u8g.setRGB(0, 0, 0);
  do {
    
    u8g.drawBox(0, 0, 128, 64);
  } while (u8g.nextPage());
}

void print_gameStart(){
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

void print_notBestScore(){
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

void print_punched(){
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

void print_bestScore(){
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

void setup(void) {

  // flip screen, if required
  //u8g.setRot180();
  

  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop(void) {

  disp_clear();
  delay(1000);
  print_gameStart();
  delay(1000);
  print_notBestScore();
  delay(1000);
  print_punched();
  delay(1000);
  print_bestScore();
  delay(1000);
  
}
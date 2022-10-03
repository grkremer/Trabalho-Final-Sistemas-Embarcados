#include <Keypad.h>
 
const byte ROWS = 8; //four rows
const byte COLS = 8; //four columns
 
//define the cymbols on the buttons of the keypads
char hexaKeys[ROWS][COLS] = {
  {1,2, 3, 4, 5, 6,7, 8},
  {9, 10, 11, 12, 13, 14, 15, 16},
  {17, 18, 19, 20, 21, 22, 23, 24},
  {25, 26, 27, 28, 29, 30, 31, 32},
  {33, 34, 35, 36, 37, 38, 39, 40},
  {41, 42, 43, 44, 45, 46, 47, 48},
  {49, 50, 51, 52, 53, 54, 55, 56},
  {57, 58, 59, 60, 61, 62, 63, 64},
};

 
byte rowPins[ROWS] = {14, 15, 16, 17, 18, 19, 20, 21}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {2, 3, 4, 5, 6, 7, 8, 9}; //connect to the column pinouts of the keypad
 
//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);
 
void setup(){
  Serial.begin(9600);
}
 
void loop(){
  char customKey = customKeypad.getKey();
  if (customKey){
        Serial.println(customKey);
  }
}
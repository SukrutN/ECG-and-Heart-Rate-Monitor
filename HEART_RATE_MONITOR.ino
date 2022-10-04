/* This program displays the Average BPM on the LED display, with an animation and a buzzer sound
* everytime a heart pulse is detected*/
 
 
#include <Adafruit_GFX.h>        //OLED libraries
#include <Adafruit_SSD1306.h>
#include <Wire.h>
#include "MAX30105.h"           //MAX3010x library
#include "heartRate.h"          //Heart rate calculating algorithm
 
MAX30105 particleSensor;
 
const byte RATE_SIZE = 5; //Increase this for more averaging. 5 is baseline
byte rates[RATE_SIZE]; //Array of heart rates
byte rateSpot = 0;
long lastBeat = 0; //Time at which the last beat occurred
float beatsPerMinute;
int beatAvg;
 
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels
#define OLED_RESET    -1 // Reset pin # (-1 if sharing Arduino reset pin)
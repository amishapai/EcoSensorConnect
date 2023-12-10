#include <Wire.h>
#include "rgb_lcd.h"  // include Seeed Studio LCD library

rgb_lcd lcd; 

// Define analog pin for the MQ sensor
const int mqSensorPin = A0;

void setup() {
 // initialize the LCD with 16 columns and 2 rows:
  lcd.begin(16, 2);
 
  // move cursor to upper left position (0, 0)
  lcd.setCursor(0, 0);
  // print text on the LCD
  lcd.print("MQ Sensor Reading");
}

void loop() {
  // Read analog value from the MQ sensor
  int sensorValue = analogRead(mqSensorPin);

  // Convert analog value to voltage
  float voltage = sensorValue * (5.0 / 1023.0);

  // Display MQ sensor readings on the LCD
  lcd.setCursor(0, 1);
  lcd.print("MQ Value: ");
  lcd.print(sensorValue);
  lcd.setCursor(0, 0);
  lcd.print("Voltage: ");
  lcd.print(voltage, 2);

  delay(1000);  // Adjust delay based on your requirements
}

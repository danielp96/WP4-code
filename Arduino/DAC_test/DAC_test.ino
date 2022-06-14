
#include <stdint.h>

#include "DAC5669.h"

//ADC5669 I2C address is (0x56)
#define DAC 0x56

DAC5669 dac(0x56);


void setup() {
  // Initialize dac
  dac.init();
  //Initialise serial communication, baud rate = 9600
  Serial.begin(9600);
  delay(300);
}

void loop() {

  dac.writeChannel(7, 0x8000, true);
  dac.writeChannel(5, 0x4000, true);
  dac.writeChannel(0, 0x8000, true);

  delay(500);

}


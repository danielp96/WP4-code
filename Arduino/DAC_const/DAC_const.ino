
#include <stdint.h>

#include "DAC5669.h"

//ADC5669 I2C address is (0x56)
#define DAC 0x56

DAC5669 dac(0x56);

uint16_t value = 0;

uint32_t time = 60000*10;

void setup()
{
  // Initialize dac
  dac.init();
  //Initialise serial communication, baud rate = 9600
  Serial.begin(9600);
  delay(300);
}

void loop()
{

    value = 0x8000;
    dac.writeChannel(0, value, false);
    dac.writeChannel(1, value, false);
    dac.writeChannel(2, value, false);
    dac.writeChannel(3, value, false);
    dac.writeChannel(4, value, false);
    dac.writeChannel(5, value, false);
    dac.writeChannel(6, value, false);
    dac.writeChannel(7, value, false);
    dac.updateAll();
    delay(time);


    value = 0; // valor de los canales durante 10 min
    dac.writeChannel(0, value, false);
    dac.writeChannel(1, value, false);
    dac.writeChannel(2, value, false);
    dac.writeChannel(3, value, false);
    dac.writeChannel(4, value, false);
    dac.writeChannel(5, value, false);
    dac.writeChannel(6, value, false);
    dac.writeChannel(7, value, false);
    dac.updateAll();
    delay(time);


}

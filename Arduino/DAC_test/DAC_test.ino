
#include <stdint.h>

#include "DAC5669.h"

//ADC5669 I2C address is (0x56)
#define DAC 0x56

DAC5669 dac(0x56);

uint16_t value = 0;

bool up = true;

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


    dac.writeChannel(0, value, false);
    dac.writeChannel(1, value, false);
    dac.writeChannel(2, value, false);
    dac.writeChannel(3, value, false);
    dac.writeChannel(4, value, false);
    dac.writeChannel(5, value, false);
    dac.writeChannel(6, value, false);
    dac.writeChannel(7, value, false);
    dac.updateAll();

    delay(10);

    if (up)
    {
        value += 1;
    }
    else
    {
        value -= 1;
    }

    if (0xFFFF == value)
    {
        up = false;
    }
    else if (0x0000 == value)
    {
        up = true;
    }

}

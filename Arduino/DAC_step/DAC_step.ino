
#include <stdint.h>

#include "DAC5669.h"

//ADC5669 I2C address is (0x56)
#define DAC 0x56

DAC5669 dac(0x56);

uint8_t msb = 0x01;
uint8_t lsb = 0x00;

bool up = true;

uint32_t time = 60000*5;

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

    dac.writeChannel(0, 0x0000, false);
    dac.writeChannel(1, 0x2000, false);
    dac.writeChannel(2, 0x4000, false);
    dac.writeChannel(3, 0x6000, false);
    dac.writeChannel(4, 0x8000, false);
    dac.writeChannel(5, 0xA000, false);
    dac.writeChannel(6, 0xC000, false);
    dac.writeChannel(7, 0xE000, false);
    dac.updateAll();
    delay(time);


    dac.writeChannel(0, 0x2000, false);
    dac.writeChannel(1, 0x4000, false);
    dac.writeChannel(2, 0x6000, false);
    dac.writeChannel(3, 0x8000, false);
    dac.writeChannel(4, 0xA000, false);
    dac.writeChannel(5, 0xC000, false);
    dac.writeChannel(6, 0xE000, false);
    dac.writeChannel(7, 0x0000, false);
    dac.updateAll();
    delay(time);


    dac.writeChannel(0, 0x4000, false);
    dac.writeChannel(1, 0x6000, false);
    dac.writeChannel(2, 0x8000, false);
    dac.writeChannel(3, 0xA000, false);
    dac.writeChannel(4, 0xC000, false);
    dac.writeChannel(5, 0xE000, false);
    dac.writeChannel(6, 0x0000, false);
    dac.writeChannel(7, 0x2000, false);
    dac.updateAll();
    delay(time);



    dac.writeChannel(0, 0x6000, false);
    dac.writeChannel(1, 0x8000, false);
    dac.writeChannel(2, 0xA000, false);
    dac.writeChannel(3, 0xC000, false);
    dac.writeChannel(4, 0xE000, false);
    dac.writeChannel(5, 0x0000, false);
    dac.writeChannel(6, 0x2000, false);
    dac.writeChannel(7, 0x4000, false);
    dac.updateAll();
    delay(time);


    dac.writeChannel(0, 0x8000, false);
    dac.writeChannel(1, 0xA000, false);
    dac.writeChannel(2, 0xC000, false);
    dac.writeChannel(3, 0xE000, false);
    dac.writeChannel(4, 0x0000, false);
    dac.writeChannel(5, 0x2000, false);
    dac.writeChannel(6, 0x4000, false);
    dac.writeChannel(7, 0x6000, false);
    dac.updateAll();
    delay(time);
    


    dac.writeChannel(0, 0xA000, false);
    dac.writeChannel(1, 0xC000, false);
    dac.writeChannel(2, 0xE000, false);
    dac.writeChannel(3, 0x0000, false);
    dac.writeChannel(4, 0x2000, false);
    dac.writeChannel(5, 0x4000, false);
    dac.writeChannel(6, 0x6000, false);
    dac.writeChannel(7, 0x8000, false);
    dac.updateAll();
    delay(time);


    dac.writeChannel(0, 0xC000, false);
    dac.writeChannel(1, 0xE000, false);
    dac.writeChannel(2, 0x0000, false);
    dac.writeChannel(3, 0x2000, false);
    dac.writeChannel(4, 0x4000, false);
    dac.writeChannel(5, 0x6000, false);
    dac.writeChannel(6, 0x8000, false);
    dac.writeChannel(7, 0xA000, false);
    dac.updateAll();
    delay(time);
    
    dac.writeChannel(0, 0xE000, false);
    dac.writeChannel(1, 0x0000, false);
    dac.writeChannel(2, 0x2000, false);
    dac.writeChannel(3, 0x4000, false);
    dac.writeChannel(4, 0x6000, false);
    dac.writeChannel(5, 0x8000, false);
    dac.writeChannel(6, 0xA000, false);
    dac.writeChannel(7, 0xC000, false);
    dac.updateAll();
    delay(time);




    dac.writeChannel(0, 0x0800, false);
    dac.writeChannel(1, 0x1000, false);
    dac.writeChannel(2, 0x2000, false);
    dac.writeChannel(3, 0x4000, false);
    dac.writeChannel(4, 0x8000, false);
    dac.writeChannel(5, 0x0100, false);
    dac.writeChannel(6, 0x0200, false);
    dac.writeChannel(7, 0x0400, false);
    dac.updateAll();
    delay(time);


    dac.writeChannel(0, 0x0400, false);
    dac.writeChannel(1, 0x0800, false);
    dac.writeChannel(2, 0x1000, false);
    dac.writeChannel(3, 0x2000, false);
    dac.writeChannel(4, 0x4000, false);
    dac.writeChannel(5, 0x8000, false);
    dac.writeChannel(6, 0x0100, false);
    dac.writeChannel(7, 0x0200, false);
    dac.updateAll();
    delay(time);

    dac.writeChannel(0, 0x0200, false);
    dac.writeChannel(1, 0x0400, false);
    dac.writeChannel(2, 0x0800, false);
    dac.writeChannel(3, 0x1000, false);
    dac.writeChannel(4, 0x2000, false);
    dac.writeChannel(5, 0x4000, false);
    dac.writeChannel(6, 0x8000, false);
    dac.writeChannel(7, 0x0100, false);
    dac.updateAll();
    delay(time);


}

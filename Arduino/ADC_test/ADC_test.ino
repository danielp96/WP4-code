
#include <stdint.h>
#include <stdbool.h>

#include "LTC2309.h"


#define address_1 0x08
#define address_2 0x18

LTC2309 adc(address_1, true);


void setup()
{

    Serial.begin(9600, true);
    adc.init();
}

void loop()
{
    Serial.println(adc.readChannel(0));
}
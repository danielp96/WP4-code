
#include <stdint.h>
#include <stdbool.h>

#include "LTC2309.h"


#define address_1 0x08
#define address_2 0x6B

LTC2309 adc(address_2, true);


void setup()
{

    Serial.begin(9600, true);
    adc.init();
}

void loop()
{
    Serial.println(String(adc.readChannel(0)));
}

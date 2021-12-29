#include "Arduino.h"
#include "PCF8591.h"
#include<Wire.h>
#define PCF8591 (0x90 >> 1)
#define AIN0 0x00
int Value = 0;

void setup()
{
  Wire.begin();
  Serial.begin(115200);
}
void loop()
{
  Wire.beginTransmission(PCF8591);
  Wire.write(AIN0);
  Wire.endTransmission();
  Wire.requestFrom(PCF8591, 1);

  Value = Wire.read();
  Serial.println("ADC Value=");
  Serial.println(Value);
  delay(500);
  
}

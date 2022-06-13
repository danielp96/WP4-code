
#include <stdint.h>
#include <Wire.h>

#include "DAC5669.h"

//ADC5669 I2C address is (0x56)
#define DAC 0x56

DAC5669 dac(0x56);


float v_in = 0;
unsigned int data[2] = {0x80, 0x00}; //start transmission with 2.5 V

void setup() {
  // Initialize I2C communication as Master
  Wire.begin();
  //Initialise serial communication, baud rate = 9600
  Serial.begin(9600);
  delay(300);
}

void loop() {

  //read input for voltage
  if (Serial.available() > 0) {
    // read the incoming byte:
    v_in = Serial.read();
    
    // say what you got:
    Serial.print("I received: ");
    Serial.println(v_in, DEC);
  }

  dac.writeChannel(7, 0x8000, true);
  dac.writeChannel(5, 0x4000, true);
  dac.writeChannel(0, 0x8000, true);
  //dacWrite(DAC_WRITE_CHANNEL_UPDATE, 7, 0x8000);
  //dacWrite(DAC_WRITE_CHANNEL_UPDATE, 5, 0x4000);

  // Convert data to display, Vref = 5 V, 16 bit resolution
  float v_out = (((data[0] * 256) + (data[1])) / 65536.0) * 5.0; 

  //Output data to serial monitor
  Serial.print("Output Voltage : ");
  Serial.print(v_out);
  Serial.println(" V");
  delay(500);

}

void dacWrite(uint8_t command, uint8_t channel, uint16_t data)
{
  channel &= 0x0F;
  command &= 0xF0;
  
  // Start I2C transmission
  Wire.beginTransmission(DAC);
  
  // Select DAC input register
  Wire.write(command | channel);
  
  // Write data 
  // MSB
  Wire.write((data >> 8) & 0x00FF);
  
  // LSB
  Wire.write(data & 0x00FF);
  
  // Stop I2C transmission
  Wire.endTransmission();
}

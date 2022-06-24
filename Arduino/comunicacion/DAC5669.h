
#include <stdint.h>
#include <stdbool.h>
#include <Wire.h>


#define DAC_WRITE_CHANNEL_UPDATE_NONE 0x00
#define DAC_UPDATE_CHANNEL            0x10
#define DAC_WRITE_CHANNEL_UPDATE_ALL  0x20
#define DAC_WRITE_CHANNEL_UPDATE      0x30
#define DAC_POWER_DOWN_UP             0x40
#define DAC_LOAD_CLEAR_CODE           0x50
#define DAC_LOAD_LDAC_CODE            0x60
#define DAC_RESET                     0x70
#define DAC_SET_INTERNAL_REF          0x80
#define DAC_ENABLE_MULTY_BYTE         0x90


class DAC5669
{
public:
    DAC5669(uint8_t address);
    void init();
    void reset();
    void updateAll();
    //void clear();
    void writeChannel(uint8_t channel, uint16_t data, bool update);
    void updateChannel(uint8_t channel);

private:
    uint8_t _address;
    uint16_t _data[8] = {0, 0, 0, 0, 0, 0, 0, 0};

    void _write(uint8_t command, uint8_t channel, uint16_t data);

};


DAC5669::DAC5669(uint8_t address)
{
  this->_address = address;
}

void DAC5669::init()
{
    Wire.begin();
}

void DAC5669::updateAll()
{
    _write(DAC_WRITE_CHANNEL_UPDATE_ALL, 0, _data[0]);
}

void DAC5669::reset()
{
    _write(DAC_RESET, 0, 0x00);
    _data[0] = 0x00;
}


void DAC5669::writeChannel(uint8_t channel, uint16_t data, bool update)
{
    _data[channel] = data;

    uint8_t command = update? DAC_WRITE_CHANNEL_UPDATE: DAC_WRITE_CHANNEL_UPDATE_NONE;

    _write(command, channel, data);
}


void DAC5669::updateChannel(uint8_t channel)
{
    _write(DAC_UPDATE_CHANNEL, channel, _data[channel]);
}


void DAC5669::_write(uint8_t command, uint8_t channel, uint16_t data)
{

  channel &= 0x0F;
  command &= 0xF0;
  
  // Start I2C transmission
  Wire.beginTransmission(this->_address);
  
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

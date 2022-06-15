
#include <stdint.h>
#include <stdbool.h>
#include <Wire.h>

#define LTC2309_CHANNEL_0 0x00
#define LTC2309_CHANNEL_2 0x10
#define LTC2309_CHANNEL_4 0x20
#define LTC2309_CHANNEL_6 0x30
#define LTC2309_CHANNEL_1 0x40
#define LTC2309_CHANNEL_3 0x50
#define LTC2309_CHANNEL_5 0x60
#define LTC2309_CHANNEL_7 0x70

#define LTC2309_MODE_SINGLE_ENDED 0x80
#define LTC2309_MODE_DIFFERENTIAL 0x00

class LTC2309
{
public:
    LTC2309(uint8_t address, bool single_ended_mode);
    void init();
    uint16_t readChannel(uint8_t channel);
    void modeDifferential();
    void modeSingleEnded();

private:
    uint8_t _address;
    uint8_t _mode;
    
};

LTC2309::LTC2309(uint8_t address, bool single_ended_mode)
{
    this->_address = address;

    this->_mode = single_ended_mode? LTC2309_MODE_SINGLE_ENDED : LTC2309_MODE_DIFFERENTIAL;
}

void LTC2309::init()
{
    Wire.begin();
}

void LTC2309::modeDifferential()
{
    this->_mode = LTC2309_MODE_DIFFERENTIAL;
}

void LTC2309::modeSingleEnded()
{
    this->_mode = LTC2309_MODE_SINGLE_ENDED;
}

uint16_t LTC2309::readChannel(uint8_t channel)
{
    channel &= 0x07;

    uint8_t command = this->_mode;

    switch (channel)
    {
        case 0:
            command |= LTC2309_CHANNEL_0;
            break;

        case 1:
            command |= LTC2309_CHANNEL_1;
            break;
            
        case 2:
            command |= LTC2309_CHANNEL_2;
            break;
            
        case 3:
            command |= LTC2309_CHANNEL_3;
            break;
            
        case 4:
            command |= LTC2309_CHANNEL_4;
            break;
            
        case 5:
            command |= LTC2309_CHANNEL_5;
            break;
            
        case 6:
            command |= LTC2309_CHANNEL_6;
            break;
            
        case 7:
            command |= LTC2309_CHANNEL_7;
            break;
    }

    // Start I2C transmission
    Wire.beginTransmission(this->_address);

    Wire.write(command);

    Wire.endTransmission();

    Wire.requestFrom(this->_address, (uint8_t)2);

    uint16_t data = 0;

    data  = Wire.read() << 8;
    data |= Wire.read();

    return data >> 4;

}
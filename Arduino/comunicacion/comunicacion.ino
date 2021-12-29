/*
 * Put a descripction and license here later.
 */

#include <stdint.h>
#include <stdlib.h>

#define BAUDRATE 9600

#define PROTOCOL_VERSION 0


#include "Arduino.h"
#include "PCF8591.h"
#define PCF8591_I2C_ADDRESS 0x48
PCF8591 pcf8591(PCF8591_I2C_ADDRESS);



// expand if needed
struct Channel
{
    bool     enabled;
    bool     timer_enabled;
    int16_t  current;       // change if needed
    uint16_t time;          // change if needed

};

struct Channel CH0_data;
struct Channel CH1_data;
struct Channel CH2_data;
struct Channel CH3_data;
struct Channel CH4_data;
struct Channel CH5_data;
struct Channel CH6_data;
struct Channel CH7_data;

struct Channel *channel_list[8] = {&CH0_data,
                                   &CH1_data,
                                   &CH2_data,
                                   &CH3_data,
                                   &CH4_data,
                                   &CH5_data,
                                   &CH6_data,
                                   &CH7_data};

bool connected2PC = false;

void setup(void)
{
    Serial.begin(BAUDRATE);

    pinMode(LED_BUILTIN, OUTPUT);

    configChannel(0, false, 0, 0);
    configChannel(1, false, 0, 0);
    configChannel(2, false, 0, 0);
    configChannel(3, false, 0, 0);
    configChannel(4, false, 0, 0);
    configChannel(5, false, 0, 0);
    configChannel(6, false, 0, 0);
    configChannel(7, false, 0, 0);

   Serial.begin(9600);
   pcf8591.begin();

}

void loop(void)
{

    processCommand();    

  float ana0V = pcf8591.voltageRead(AIN0);
  float ana1V = pcf8591.voltageRead(AIN1);
  float ana2V = pcf8591.voltageRead(AIN2);
  float ana3V = pcf8591.voltageRead(AIN3);
  int ana0VB = pcf8591.analogRead(AIN0);
  int ana1VB = pcf8591.analogRead(AIN1);
  int ana2VB = pcf8591.analogRead(AIN2);
  int ana3VB = pcf8591.analogRead(AIN3);

  Serial.print(",");
  Serial.print(ana0VB);     // CH 0
  Serial.print(",");
  Serial.print(ana0V, 5);
  
  Serial.print(",");     // CH 1
  Serial.print(ana1VB);
  Serial.print(",");
  Serial.print(ana1V, 5);

  Serial.print(",");     // CH 2
  Serial.print(ana2VB);
  Serial.print(",");
  Serial.print(ana2V, 5);

  Serial.print(",");     // CH 3
  Serial.print(ana3VB);
  Serial.print(",");
  Serial.print(ana3V, 5);

  int canal_1;
  float canal;
  if (Serial.available())
    {
       canal_1 = Serial.parseInt();
       canal = canal_1*1.0;
    } 
  pcf8591.analogWrite(canal_1); // para bits, si es voltaje se usa pcf8591.voltageWrite(canal)
  
  Serial.print(",");
  Serial.print(canal_1);
  Serial.println(",");
   
  digitalWrite(LED_BUILTIN, connected2PC);
}

// process incoming commands
// doesn't return anything
// it sets sketch variables acording to what should be done.
// details about each command inside
// al commands should start with '$' as first character
// example: $COMMAND:ARG1;ARG2;ARG3;
void processCommand()
{

    String data;

    // check if incoming message
    if (Serial.available())
    {
        data = Serial.readStringUntil('\n');
    }
    else
    {
        return;
    }

    // check if device command
    if (data[0] != '$')
    {
        data = "";
        return;
    }

    // get command
    // example:  PING from $PING:0
    String msg = data.substring(1, data.indexOf(':'));

    // get arguments
    // example: N,A,T $SET_ONE:N,A,T;
    String args = data.substring(data.indexOf(':')+1);


    /*
     * PING command
     * Format: $PING:n
     *         where n is PROTOCOL_VERSION
     *
     * It checks that the protocol version of the pc and the device 
     * (to allow for compatibility with any future modifications)
     *
     * It only sets the status of connect to the pc.
     */

    if (msg == "PING")
    {
        connected2PC = true;
        Serial.println("PONG:0");
        return;
    }


    /*
     * SET_EACH command
     * Format: $SET_EACH:E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;
     *         where E is if the channel is enabled or disabled (1 or 0)
     *               A is current in micro amperes
     *               T is time in minutes (-1 to run until manually stopped)
     *
     * Prepares the current and time of all channels in order (CH1;CH2;CH3;...)
     * The START command should be issued after to time and current to start.
     * 
     * It sets the apropiete variables of each channel.
     */

    if (msg == "SET_EACH")
    {

        bool enable = false;
        int16_t current = 0;
        int16_t time = 0;

        for (int i=0; i<8; i++)
        {
            char* str_data = args.c_str();

            // parse string to numbers
            // +1 to skip value separator
            enable  = strtoul(str_data,   &str_data, 10);
            current =  strtol(str_data+1, &str_data, 10);
            time    =  strtol(str_data+1, &str_data, 10);

            configChannel(i, enable, current, time);

            // next channel
            args = args.substring(args.indexOf(';')+1);
        }

        Serial.println("DONE, SET_EACH");
        return;
    }

    /*
     * SET_ONE command
     * Format: $SET_ONE:N,A,T;
     *         where N is the channel number
     *               A is current in micro amperes
     *               T is time in minutes (-1 to run until manually stopped)
     *
     * Prepares the current and time of specified channel
     * The START command should be issued after to time and current to start.
     * 
     * It sets the apropiete variable of the specified channel.
     */
    if (msg == "SET_ONE")
    {
        char* str_data = args.c_str();

        // parse string to numbers
        // +1 to skip value separator
        uint8_t channel = strtoul(str_data,   &str_data, 10);
        int16_t current =  strtol(str_data+1, &str_data, 10);
        int16_t time    =  strtol(str_data+1, &str_data, 10);

        configChannel(channel, true, current, time);
        

        Serial.println("DONE, SET_ONE");
        return;
    }

    /*
     * SET_ALL command
     * Format: $SET_ALL:A,T;
     *         where A is current in micro amperes
     *               T is time in minutes (-1 to run until manually stopped)
     *
     * Prepares the current and time of all channels with the same values.
     * The START command should be issued after to time and current to start.
     * 
     * It sets the apropiete variables of each channel.
     */

    if (msg == "SET_ALL")
    {
        char* str_data = args.c_str();

        // parse string to numbers
        // +1 to skip value separator
        int16_t current =  strtol(str_data, &str_data, 10);
        int16_t time    =  strtol(str_data+1, &str_data, 10);

        configChannel(0, true, current, time);
        configChannel(1, true, current, time);
        configChannel(2, true, current, time);
        configChannel(3, true, current, time);
        configChannel(4, true, current, time);
        configChannel(5, true, current, time);
        configChannel(6, true, current, time);
        configChannel(7, true, current, time);

        Serial.println("DONE, SET_ALL");
        return;
    }


    /*
     * START command
     * Format: $START:
     *
     * Starts the experiment
     * 
     * It sets each DAC with its apropiate value
     * and starts counting time as specified.
     *
     */

    if (msg == "START")
    {
        // code goes here

        Serial.println("STARTED");
        return;
    }


    /*
     * STOP command
     * Format: $STOP:
     *
     * Stops the experiment
     * 
     * It powers off all channels and resets all timers.
     *
     */

    if (msg == "STOP")
    {
        // code goes here

        Serial.println("STOPPED");
        return;
    }


    /*
     * CALIBRATE command
     * Format: $CALIBRATE:
     *
     * Runs calibration tests and saves calibratoindata to device eeprom and to pc
     * 
     * It powers off all channels and resets all timers.
     *
     */

    if (msg == "CALIBRATE")
    {
        // code goes here

        Serial.println("CALIBRATED");
        return;
    }


    /*
     * PRINT_CONFIG command
     * Format: $PRINT_CONFIG:
     *
     * Prints to serial the configuration of all channels
     *
     */

    if (msg == "PRINT_CONFIG")
    {
        Serial.print("CHANNELS_DATA:");

        for (int i=0; i<8; i++)
        {
            Serial.print(channel_list[i]->enabled);
            Serial.print(",");
            Serial.print(channel_list[i]->timer_enabled);
            Serial.print(",");
            Serial.print(channel_list[i]->current);
            Serial.print(",");
            Serial.print(channel_list[i]->time);
            Serial.print(";");
        }

        return;
    }
}

void configChannel(uint8_t channel, bool enable, int16_t current, int16_t time)
{
    if (channel > 7)
    {
        return;
    }

    channel_list[channel]->enabled = enable;
    channel_list[channel]->timer_enabled = (enable && (time>0));
    channel_list[channel]->current = current;
    channel_list[channel]->time = time>0?time:-time;
}

/*
 * Put a descripction and license here later.
 */

#include <stdint.h>
#include <stdlib.h>

#define BAUDRATE 9600

#define PROTOCOL_VERSION 0

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

    configChannel(0, false, false, 0, 0);
    configChannel(1, false, false, 0, 0);
    configChannel(2, false, false, 0, 0);
    configChannel(3, false, false, 0, 0);
    configChannel(4, false, false, 0, 0);
    configChannel(5, false, false, 0, 0);
    configChannel(6, false, false, 0, 0);
    configChannel(7, false, false, 0, 0);

}

void loop(void)
{

    processCommand();  

    //Serial.print("DATA:0,1,2,3,4,5,6,7;");

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
     * Format: $SET_EACH:E,E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;E,A,T;
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
        // code goes here

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

        
        uint8_t channel = strtoul(str_data, &str_data, 10);
        
        int16_t current = strtol(str_data+1, &str_data, 10);
        
        int16_t time = strtol(str_data+1, &str_data, 10);

        configChannel(channel, true, (time>0), current, time);
        

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
        // code goes here

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

void configChannel(uint8_t channel, bool enable, bool timer_enable, int16_t current, uint16_t time)
{
    if (channel > 7)
    {
        return;
    }

    channel_list[channel]->enabled = enable;
    channel_list[channel]->timer_enabled = timer_enable;
    channel_list[channel]->current = current;
    channel_list[channel]->time = time;
}
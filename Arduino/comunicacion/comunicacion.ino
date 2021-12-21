/*
 * Put a descripction and license here later.
 */

#include <stdint.h>

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

struct Channel CH1_data;
struct Channel CH2_data;
struct Channel CH3_data;
struct Channel CH4_data;
struct Channel CH5_data;
struct Channel CH6_data;
struct Channel CH7_data;
struct Channel CH8_data;


bool connected2PC = false;

void setup(void)
{
    Serial.begin(BAUDRATE);

    pinMode(LED_BUILTIN, OUTPUT);

}

void loop(void)
{

    processCommand();    

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
        Serial.print("PONG:0\n");
    }


    /*
     * SET_EACH command
     * Format: $SET_EACH:A,T;A,T;A,T;A,T;A,T;A,T;A,T;A,T;
     *         where A is current in micro amperes
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

        Serial.print("DONE, SET_EACH\n");
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
        // code goes here

        Serial.print("DONE, SET_ONE\n");
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

        Serial.print("DONE, SET_ALL\n");
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

        Serial.print("STARTED\n");
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

        Serial.print("STOPPED\n");
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

        Serial.print("CALIBRATED\n");
    }
}


/*
 *refine later, just ping prototype for now
 *
 * Protocol idea:
 * -ping
 *  to help detect which port the device is in
 *  receives PING:N where N is the max protocol version program supports
 *  answers  PONG:N where N is the max protocol version device supports
 */

#define BAUDRATE 9600

String data;

bool status = false;

void setup(void)
{
    Serial.begin(BAUDRATE);

    pinMode(LED_BUILTIN, INPUT);

}

void loop(void)
{

    if (Serial.available())
    {
        data = Serial.readStringUntil('\n');
    }

    // discard data
    if ((data.length() < 4) || (data == ""))
    {
        data = "";
        return;
    }


    if (data.substring(0,4) == "PING")
    {
        Serial.print("PONG:0\n");
        status = true;
    }
    else
    {
        Serial.print("INVALID\n");
        status = false;
    }

    data = "";
    digitalWrite(LED_BUILTIN, status);
}


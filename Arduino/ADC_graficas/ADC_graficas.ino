int analogPin3 = A3; // potentiometer wiper (middle terminal) connected to analog pin 
int analogPin4 = A4; // potentiometer wiper (middle terminal) connected to analog pin 3
                    
                    
int val3 = 0;  // variable to store the value read
int val4 = 0;  // variable to store the value read

void setup() {
  Serial.begin(9600);           //  setup serial
}

void loop() {
  val3 = analogRead(analogPin3);  // read the input pin
  val4 = analogRead(analogPin4);  // read the input pin
  //Serial.print("DATA:");         // debug value
  Serial.print(val3);         // debug value
  Serial.print(",");         // debug value
  Serial.print(val4);         // debug value
  //Serial.println(",0,0,0,0,0,0;");         // debug value
  Serial.print(",");         // debug value
  Serial.print(500);
  Serial.print(",");         // debug value
  Serial.println(999);
  delay(1000);
}

// DATA:8454,2097,0,4650,0,0,0,0;

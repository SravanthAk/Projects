//set pin numbers
//const won't change
const int ledPin = 13;   //the number of the LED pin
const int ldrPin = A0;  //the number of the LDR pin
int sensorvalue = 0;


void setup() {

  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);  //initialize the LED pin as an output
  pinMode(ldrPin, INPUT);   //initialize the LDR pin as an input
}

void loop() {

  int ldrStatus = analogRead(ldrPin);   //read the status of the LDR value
  sensorvalue = analogRead(ldrPin);
  //check if the LDR status is <= 300
  //if it is, the LED is HIGH
   Serial.println(sensorvalue);

   if (sensorvalue >1000) {

    digitalWrite(ledPin, HIGH);               //turn LED off
    
   }
  else {

    digitalWrite(ledPin, LOW);          //turn LED on
  }
}

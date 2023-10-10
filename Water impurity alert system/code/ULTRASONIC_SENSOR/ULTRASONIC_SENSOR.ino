int trigPin = 7;int echoPin = 9;int led = 7;
void setup() {
   Serial.begin(9600); 
   pinMode(led, OUTPUT);pinMode(trigPin, OUTPUT);pinMode(echoPin, INPUT);
}
void loop() {
  long duration, distance;
  digitalWrite(trigPin,HIGH);delayMicroseconds(2);
  digitalWrite(trigPin, LOW);
  duration=pulseIn(echoPin, HIGH);
  distance =(duration*0.034/2);
  Serial.print(distance);
  Serial.println("CM");delay(1000);
}

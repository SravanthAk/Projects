void setup() {
  Serial.begin(9600); 
}
void loop() {
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5 / 1024.0); 
  Serial.println(voltage); 
  delay(1000);
}

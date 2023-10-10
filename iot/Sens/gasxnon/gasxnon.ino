int sensorValue;
int digitalValue;
void setup()
{

Serial.begin(9600);
pinMode( 2, INPUT);
}


void loop()

{

sensorValue = analogRead(0);

digitalValue = digitalRead(2); 
Serial.println(sensorValue, DEC);
Serial.println(digitalValue, DEC);
delay(1000);

}

#define BLYNK_PRINT Serial
#include <ESP8266_Lib.h>
#include <BlynkSimpleShieldEsp8266.h>
char auth[] = "_is4624C9fTgwxN-eUntKDoDXu8apjVZ";
char ssid[] = "pubg";
char pass[] = "yaHoo111@";
#include <SoftwareSerial.h>
SoftwareSerial EspSerial(2, 3); // RX, TX
#define ESP8266_BAUD 9600
ESP8266 wifi(&EspSerial);
BlynkTimer timer;
void setup()
{
  Serial.begin(9600);
  pinMode(A0,INPUT);
  EspSerial.begin(ESP8266_BAUD);
  delay(10);
  Blynk.begin(auth, wifi, ssid, pass);
  timer.setInterval(1000L, sendSensor);
}
void loop()
{
  Blynk.run();
  timer.run();
}
void sendSensor()
{
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1024.0); 
  Serial.println(voltage); 
  delay(1000);
  if(voltage <= 5)
  {
    Blynk.notify("Its time to clean");
  }
  Blynk.virtualWrite(V0, voltage);
  delay(1000);                        
}

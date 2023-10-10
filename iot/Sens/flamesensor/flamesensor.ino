const int led = D2;
const int flamePin = D0;
int Flame = HIGH;

void setup() 
{
  pinMode(led, OUTPUT);
  pinMode(flamePin, INPUT);
  Serial.begin(9600);
}

void loop() 
{
  Flame = digitalRead(flamePin);
  if (Flame== HIGH)
  {
    Serial.println("Fire!!!");
    digitalWrite(led,HIGH  );
  }
  else
  {
    Serial.println("No worries");
    digitalWrite(led, LOW);
  }
}

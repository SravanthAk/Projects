int trigPin = 9;
int echoPin = 10;
int led1 = 7;
int led2 = 8;

const int ldrPin = A0;  //the number of the LDR pin


void setup() {
  Serial.begin(9600); 
   pinMode(led1, OUTPUT);
   pinMode(led2, OUTPUT);
   pinMode(trigPin, OUTPUT);
   pinMode(echoPin, INPUT);
   pinMode(ldrPin, INPUT);   //initialize the LDR pin as an input
  // put your setup code here, to run once:

}

void loop() {
  int ldrStatus = analogRead(ldrPin);   //read the status of the LDR value
  long duration, distance;
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin, LOW);
  duration=pulseIn(echoPin, HIGH);
  distance =(duration/2)/29.1;
  Serial.print(distance);
  Serial.println("CM");
  delay(10);
 
 if((distance<=100)&&(ldrStatus >1000)) 
  {
    digitalWrite(led1, HIGH);
}
   else 
 {
     digitalWrite(led1, LOW);
   }
  
 if((distance>100)||(ldrStatus <=1000)) 
  {
    digitalWrite(led2, HIGH);
}
   else 
 {
     digitalWrite(led2, LOW);
   }
   

}   

#include <Servo.h>. 
const int trigPin = 10;
const int echoPin = 11;
int light_sensor = A3;
long duration;
int distance;
Servo myServo;
void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  myServo.attach(12);
  Serial.begin(9600);
  pinMode(5,OUTPUT);
}
void loop() {
  int raw_light = analogRead(light_sensor);
  int light = map(raw_light, 0, 1023, 0, 100);
  Serial.print("Light level: "); 
  Serial.println(light);
  if(light>=20) digitalWrite(5,LOW);
  else
  {
    digitalWrite(5,HIGH);
    for(int i=0;i<=180;i++)
    {  
      myServo.write(i);
      delay(30);
      distance = calculateDistance();
      Serial.print(i);
      Serial.print(",");
      Serial.print(distance);
      Serial.print(".");
    }
    for(int i=180;i>=0;i--)
    {  
      myServo.write(i);
      delay(30);
      distance = calculateDistance();
      Serial.print(i);
      Serial.print(",");
      Serial.print(distance);
      Serial.print(".");
    }
  }
}
int calculateDistance(){
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  return distance;
}

 

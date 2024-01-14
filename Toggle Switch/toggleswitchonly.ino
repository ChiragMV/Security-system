//With appropriate connections, you can link this with the rest of the project to create a lock pattern with laser security along with face detection.

void setup() {
  Serial.begin(9600); //begin Serial Communication
  pinMode(2,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);
  pinMode(6,INPUT_PULLUP);
  pinMode(8,INPUT_PULLUP);
  pinMode(9,INPUT_PULLUP);
  pinMode(10,INPUT_PULLUP);
  pinMode(13,OUTPUT);
}
 
void loop() {

  if(digitalRead(3)==HIGH && digitalRead(5)==HIGH && digitalRead(7)==HIGH && analogRead(A0)>500 && digitalRead(A1)==HIGH && digitalRead(11)==HIGH)
  {
    digitalWrite(13,HIGH);
    Serial.println(digitalRead(11));
  }
  else
  {
    digitalWrite(13,LOW);
  }
}

#include <Servo.h>
Servo motor;
int ledBottle = 12;
int ledPlastic = 13;
int ledGreen = 9;
int ledWhite = 11;
int ledMalta = 7;
int ledColor = 8;
int ledTrans = 10;
int option;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledBottle, OUTPUT);
  pinMode(ledPlastic, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledWhite, OUTPUT);
  pinMode(ledMalta, OUTPUT);
  pinMode(ledColor, OUTPUT);
  pinMode(ledTrans, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    option = Serial.read();
    if (option == 'B')
    {
      digitalWrite(ledBottle, HIGH);
      delay(250);
    } else if (option == 'b')
    {
      digitalWrite(ledBottle, LOW);
      delay(250);
    } else if (option == 'P')
    {
      digitalWrite(ledPlastic, LOW);
    } else if (option == 'p')
    {
      digitalWrite(ledPlastic, HIGH);
    } else if (option == 'g')
    {
      digitalWrite(ledGreen, HIGH);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
      delay(800);
    } else if (option == 'w')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, HIGH);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
      delay(800);
    } else if (option == 'm')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, HIGH);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
      delay(800);
    } else if (option == 't')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, HIGH);
      delay(800);
    } else if (option == 'c')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, HIGH);
      digitalWrite(ledTrans, LOW);
      delay(800);
    }else {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
    }
  }
}

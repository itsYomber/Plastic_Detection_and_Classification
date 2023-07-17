#include <Servo.h>
Servo motor;
int ledBottle = 13;
int MotorPlastic = 12;
int ledGreen = 11;
int ledWhite = 10;
int ledMalta = 9;
int ledColor = 8;
int option;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledBottle, OUTPUT);
  motor.attach(MotorPlastic);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledWhite, OUTPUT);
  pinMode(ledMalta, OUTPUT);
  pinMode(ledColor, OUTPUT);
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
      motor.write(80);
    } else if (option == 'p')
    {
      motor.write(20);
    } else if (option == 'g')
    {
      digitalWrite(ledGreen, HIGH);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      delay(800);
    } else if (option == 'w')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, HIGH);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      delay(800);
    } else if (option == 'm')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, HIGH);
      digitalWrite(ledColor, LOW);
      delay(800);
    } else if (option == 't')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      delay(800);
    } else if (option == 'c')
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, HIGH);
      delay(800);
    }else {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
    }
  }
}

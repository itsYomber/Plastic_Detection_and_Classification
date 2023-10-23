// declaración de variables
int ledBottle = 12;
int ledPlastic = 13;
int ledGreen = 9;
int ledWhite = 11;
int ledMalta = 7;
int ledColor = 8;
int ledTrans = 10;
int option;

void setup() {
  // inicialización de frecuencia de trabajo y pines a usar
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
  // verificación de ingreso de información
  if (Serial.available() > 0){
    option = Serial.read();
    if (option == 'B')         // detección de botella
    {
      digitalWrite(ledBottle, HIGH);
      delay(250);
    } else if (option == 'b')  // no detección de botella
    {
      digitalWrite(ledBottle, LOW);
      delay(250);
    } else if (option == 'P')  // detección de plástico
    {
      digitalWrite(ledPlastic, LOW);
    } else if (option == 'p')  // no detección de plástico
    {
      digitalWrite(ledPlastic, HIGH);
    } else if (option == 'g')  // verde detectado
    {
      digitalWrite(ledGreen, HIGH);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
      delay(800);
    } else if (option == 'w')  // blanco detectado
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, HIGH);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
      delay(800);
    } else if (option == 'm')  // malta detectado
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, HIGH);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
      delay(800);
    } else if (option == 't')  // transparente detectado
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, HIGH);
      delay(800);
    } else if (option == 'c')  // color detectado
    {
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, HIGH);
      digitalWrite(ledTrans, LOW);
      delay(800);
    }else {                    // ningún color detectado
      digitalWrite(ledGreen, LOW);
      digitalWrite(ledWhite, LOW);
      digitalWrite(ledMalta, LOW);
      digitalWrite(ledColor, LOW);
      digitalWrite(ledTrans, LOW);
    }
  }
}

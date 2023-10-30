#include <string.h>

#define enA 9
#define in1 4
#define in2 5
#define enB 10
#define in3 6
#define in4 7

int motorSpeedA = 0;
int motorSpeedB = 0;

void setup() {
  Serial.begin(9600);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

String data(){
  String readstring = "";
  if(Serial.available()){
    char c = Serial.read();
    readstring += c;
  }
}
void loop() {
  String command = data();
  char option = command[0];
  int variator;
  if(command.length() != 1) {
    String a = command.substring(1);
    variator = a.toInt();
    }

  if(option == '1'){
     digitalWrite(in1, LOW);
     digitalWrite(in2, HIGH);
     digitalWrite(in3, LOW);
     digitalWrite(in4, HIGH);
     motorSpeedA = variator;
     motorSpeedB = variator;
     analogWrite(enA, motorSpeedA);
     analogWrite(enB, motorSpeedB);
  }

  else if(option == '2'){
     digitalWrite(in2, LOW);
     digitalWrite(in1, HIGH);
     digitalWrite(in4, LOW);
     digitalWrite(in3, HIGH);
     motorSpeedA = variator;
     motorSpeedB = variator;
     analogWrite(enA, motorSpeedA);
     analogWrite(enB, motorSpeedB);
  }

  else if(option == '5'){
     digitalWrite(in2, LOW);
     digitalWrite(in1, HIGH);
     digitalWrite(in4, LOW);
     digitalWrite(in3, HIGH);
     motorSpeedA = 0;
     motorSpeedB = 0;
     analogWrite(enA, motorSpeedA);
     analogWrite(enB, motorSpeedB);
  }

  else if(option == '3'){
     digitalWrite(in1, LOW);
     digitalWrite(in2, HIGH);
     digitalWrite(in4, LOW);
     digitalWrite(in3, HIGH);
     motorSpeedA = 20;
     motorSpeedB = 5;
     analogWrite(enA, motorSpeedA);
     analogWrite(enB, motorSpeedB);
  }

  else if(option == '4'){
     digitalWrite(in2, LOW);
     digitalWrite(in1, HIGH);
     digitalWrite(in3, LOW);
     digitalWrite(in4, HIGH);
     motorSpeedA = 5;
     motorSpeedB = 20;
     analogWrite(enA, motorSpeedA);
     analogWrite(enB, motorSpeedB);
  }
}

const int pinBleu = A3;
const int pinJaune = A2;
const int pinVert = A4;
const int pinRouge = A5;

const int delai = 400;
const int seuil = 450;

void setup() {
  pinMode(pinBleu, INPUT);
  pinMode(pinJaune, INPUT);
  pinMode(pinVert, INPUT);
  pinMode(pinRouge, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (analogRead(pinBleu) > 460) {
    Serial.println("B");
    while (analogRead(pinBleu) > 440) {
      delay(delai);
    }
  }
  if (analogRead(pinJaune) > 380) {
    Serial.println("Y");
    while (analogRead(pinJaune) > 310) {
      delay(delai);
    }
  }
  if (analogRead(pinVert) > 380) {
    Serial.println("G");
    while (analogRead(pinVert) > 310) {
      delay(delai);
    }
  }
  if (analogRead(pinRouge) > 370) {
    Serial.println("R");
    while (analogRead(pinRouge) > 320) {
      delay(delai);
    }
  }
  delay(delai);
}
const int pinBleu = A0;
const int pinJaune = A2;
const int pinVert = A4;
const int pinRouge = A5;

const int seuil = 420;
const int delai = 900;

void setup() {
  pinMode(pinBleu, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (analogRead(pinBleu) > seuil) {
    Serial.println("B");
    while (analogRead(pinBleu) > seuil-65) {
      delay(delai);
    }
  }
  if (analogRead(pinJaune) > seuil) {
    Serial.println("Y");
    while (analogRead(pinJaune) > seuil-65) {
      delay(delai);
    }
  }
  if (analogRead(pinVert) > seuil) {
    Serial.println("G");
    while (analogRead(pinVert) > seuil-65) {
      delay(delai);
    }
  }
  if (analogRead(pinRouge) > seuil) {
    Serial.println("R");
    while (analogRead(pinRouge) > seuil-65) {
      delay(delai);
    }
  }
  delay(delai);
}
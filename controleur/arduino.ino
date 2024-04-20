const int pinBleu = A1;
const int pinRouge = A2;
const int pinJaune = A3;
const int pinVert = A5;

const int seuil = 850;
const int delai = 100;

void setup() {
  pinMode(pinBleu, INPUT);
  pinMode(pinRouge, INPUT);
  pinMode(pinJaune, INPUT);
  pinMode(pinVert, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (analogRead(pinBleu) > seuil) {
    Serial.println("B");
    while (analogRead(pinBleu) > seuil) {
      delay(delai);
  }
  }
  if (analogRead(pinRouge) > seuil) {
    Serial.println("R");
    while (analogRead(pinRouge) > seuil) {
      delay(delai);
    }
  }
  if (analogRead(pinVert) > seuil) {
    Serial.println("G");
    while (analogRead(pinVert) > seuil) {
      delay(delai);
    }
  }
  if (analogRead(pinJaune) > seuil) {
    Serial.println("Y");
    while (analogRead(pinJaune) > seuil) {
      delay(delai);
    }
  }
  delay(delai);
}
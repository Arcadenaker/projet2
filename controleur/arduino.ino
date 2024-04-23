const int pinBleu = A1;
const int pinRouge = A2;
const int pinJaune = A3;
const int pinVert = A5;

const int seuil_haut = 400; // Seuil haut pour la détection de tension
const int seuil_bas = 300;  // Seuil bas pour la détection de tension
const int delai = 100;

void setup() {
  pinMode(pinBleu, INPUT);
  pinMode(pinRouge, INPUT);
  pinMode(pinJaune, INPUT);
  pinMode(pinVert, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (analogRead(pinBleu) > seuil_haut) {
    Serial.println("B");
    while (analogRead(pinBleu) > seuil_bas) {} // Attend que la tension redescende en dessous du seuil bas
  }
  if (analogRead(pinRouge) > seuil_haut) {
    Serial.println("R");
    while (analogRead(pinRouge) > seuil_bas) {}
  }
  if (analogRead(pinVert) > seuil_haut) {
    Serial.println("G");
    while (analogRead(pinVert) > seuil_bas) {}
  }
  if (analogRead(pinJaune) > seuil_haut) {
    Serial.println("Y");
    while (analogRead(pinJaune) > seuil_bas) {}
  }
  delay(delai);
}

const int pinBleu = 0;   // GPIO0
const int pinRouge = 2;  // GPIO2
const int pinJaune = 4;  // GPIO4
const int pinVert = 5;   // GPIO5
const int seuil = 100;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Lire les tensions sur les broches analogiques
  int valeurBleu = analogRead(pinBleu);
  int valeurRouge = analogRead(pinRouge);
  int valeurJaune = analogRead(pinJaune);
  int valeurVert = analogRead(pinVert);
  
  // Vérifier quelle broche a une tension significative
  if (valeurBleu > seuil) {
    Serial.print("B");
    // Attendre jusqu'à ce que la tension redescende en dessous du seuil
    while (analogRead(pinBleu) > seuil) {
      delay(100);
    }
  }
  if (valeurRouge > seuil) {
    Serial.print("R");
    while (analogRead(pinRouge) > seuil) {
      delay(100);
    }
  }
  if (valeurJaune > seuil) {
    Serial.print("Y");
    while (analogRead(pinJaune) > seuil) {
      delay(100);
    }
  }
  if (valeurVert > seuil) {
    Serial.print("G");
    while (analogRead(pinVert) > seuil) {
      delay(100);
      }
  }
  
  delay(100); // Attendre un peu avant de lire à nouveau
}
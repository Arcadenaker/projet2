// Définition des broches pour les capteurs de couleurs
const int pinBleu = A3;
const int pinJaune = A2;
const int pinVert = A4;
const int pinRouge = A5;

// Durée de délai entre les lectures des capteurs
const int delai = 400;

void setup() {
  // Définir les broches comme entrées
  pinMode(pinBleu, INPUT);
  pinMode(pinJaune, INPUT);
  pinMode(pinVert, INPUT);
  pinMode(pinRouge, INPUT);
  
  // Initialiser la communication série à 9600 bauds
  Serial.begin(9600);
}

void loop() {
  // Vérifier si la pin de la couleur bleue détecte une couleur
  if (analogRead(pinBleu) > 460) {
    // Envoyer "B" avec Serial
    Serial.println("B");
    // Attendre que la couleur bleue passe en dessous du seuil bas
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
  if (analogRead(pinVert) > 370) {
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
  // Attendre un délai avant la prochaine itération de la boucle
  delay(delai);
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPi.h>
#include <wiringSerial.h>

#define PIN_BLEU 1
#define PIN_ROUGE 4
#define PIN_JAUNE 5
#define PIN_VERT 6

#define SEUIL 850
#define DELAI 100

int main() {
    wiringPiSetup();

    pinMode(PIN_BLEU, INPUT);
    pinMode(PIN_ROUGE, INPUT);
    pinMode(PIN_JAUNE, INPUT);
    pinMode(PIN_VERT, INPUT);

    char port[20];
    int serial_port = -1;
    char choix[20];

    printf("Entrez le nom du port série de votre adaptateur WiFi USB : ");
    scanf("%s", choix);

    serial_port = serialOpen(choix, 9600);
    if (serial_port < 0) {
        fprintf(stderr, "Impossible d'ouvrir le port série %s.\n", choix);
        return 1;
    }

    printf("Port série %s ouvert avec succès.\n", choix);

    while(1) {
        if (analogRead(PIN_BLEU) > SEUIL) {
            serialPuts(serial_port, "B\n");
            while (analogRead(PIN_BLEU) > SEUIL) {
                delay(DELAI);
            }
        }
        if (analogRead(PIN_ROUGE) > SEUIL) {
            serialPuts(serial_port, "R\n");
            while (analogRead(PIN_ROUGE) > SEUIL) {
                delay(DELAI);
            }
        }
        if (analogRead(PIN_VERT) > SEUIL) {
            serialPuts(serial_port, "G\n");
            while (analogRead(PIN_VERT) > SEUIL) {
                delay(DELAI);
            }
        }
        if (analogRead(PIN_JAUNE) > SEUIL) {
            serialPuts(serial_port, "Y\n");
            while (analogRead(PIN_JAUNE) > SEUIL) {
                delay(DELAI);
            }
        }
        delay(DELAI);
    }

    return 0;
}

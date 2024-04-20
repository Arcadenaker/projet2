#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPi.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>

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

    // Configuration de l'adresse IP et du point d'accès Wi-Fi
    const char *wifi_interface = "wlan0";
    const char *wifi_ssid = "MonPointDacces";
    const char *wifi_password = "MotDePasse";

    // Configuration de l'adresse IP et du port
    const char *server_ip = "192.168.4.1"; // Adresse IP du serveur Wi-Fi
    int server_port = 8888; // Port à utiliser

    // Configurer l'interface Wi-Fi
    system("sudo ip link set dev wlan0 down");
    system("sudo ip addr flush dev wlan0");
    system("sudo ip link set dev wlan0 up");
    system("sudo ip addr add 192.168.4.1/24 broadcast 192.168.4.255 dev wlan0");

    // Lancement du service DHCP
    system("sudo service dnsmasq restart");

    // Lancement du point d'accès
    system("sudo hostapd -B /etc/hostapd/hostapd.conf");

    // Création de la socket
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Erreur lors de la création de la socket");
        return 1;
    }

    // Configuration de l'adresse du serveur
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port);
    inet_pton(AF_INET, server_ip, &server_addr.sin_addr);

    // Attente de connexion des clients
    int client_sockfd;
    struct sockaddr_in client_addr;
    socklen_t client_len = sizeof(client_addr);

    while (1) {
        client_sockfd = accept(sockfd, (struct sockaddr *)&client_addr, &client_len);
        if (client_sockfd < 0) {
            perror("Erreur lors de l'acceptation de la connexion client");
            continue;
        }

        while (1) {
            if (analogRead(PIN_BLEU) > SEUIL) {
                send(client_sockfd, "B\n", 2, 0);
                while (analogRead(PIN_BLEU) > SEUIL) {
                    delay(DELAI);
                }
            }
            if (analogRead(PIN_ROUGE) > SEUIL) {
                send(client_sockfd, "R\n", 2, 0);
                while (analogRead(PIN_ROUGE) > SEUIL) {
                    delay(DELAI);
                }
            }
            if (analogRead(PIN_VERT) > SEUIL) {
                send(client_sockfd, "G\n", 2, 0);
                while (analogRead(PIN_VERT) > SEUIL) {
                    delay(DELAI);
                }
            }
            if (analogRead(PIN_JAUNE) > SEUIL) {
                send(client_sockfd, "Y\n", 2, 0);
                while (analogRead(PIN_JAUNE) > SEUIL) {
                    delay(DELAI);
                }
            }
            delay(DELAI);
        }
    }

    close(sockfd);
    return 0;
}
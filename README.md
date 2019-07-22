# Plascilab-RPi-RFID
Module Python permettant la lecture de badges RFID et l'envoi de l'identifiant unique du badge sur le réseau ethernet. Conçu pour le FabLab de Planète Sciences - Plascilab.

__Site du Plascilab :__ <https://www.plascilab.fr/>

__Site de Planète Sciences :__ <http://www.planete-sciences.org/national/>

# Utilisation du module

## Téléchargement et installation

### Installer les bibliothèques nécéssaires

Le module Plascilab-RPi-RFID utilise plusieurs bibliothèques pour fonctionner :

* __spidev__, pour gérer l'interface SPI ;
* __MFRC522__, pour gérer le lecteur RFID.

Pour installer ces deux bibliothèques, ouvrez un terminal sur le Raspberry PI (_via_ une session SSH ou directement en branchant un clavier et un écran au Raspberry) et entrez les deux commandes suivantes :

`sudo pip3 install spidev`

`sudo pip3 install mfrc522`

### Activer l'interface SPI

L'interface SPI permet de communiquer avec le lecteur RFID. Pour l'activer, ouvrez un terminal sur le Raspberry et entrez dans la configuration de la carte en tapant `sudo raspi-config`. Avec les touches du clavier, navigez vers __"5 Interfacing Options"__

Pour télécharger le module, cliquez sur le bouton "Clone or download" puis sur "Download ZIP".

Extrayez ensuite le fichier où vous le souhaitez. Copiez le contenu du dossier `pi-rfid` sur le Raspberry PI _via_ une session SSH ou directement en mode graphique. Vous pouvez également cloner ce dépôt git  

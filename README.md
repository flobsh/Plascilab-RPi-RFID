# Plascilab-RPi-RFID
Module Python permettant la lecture de badges RFID et l'envoi de l'identifiant unique du badge sur le réseau ethernet. Conçu pour le FabLab de Planète Sciences - Plascilab.

__Site du Plascilab :__ <https://www.plascilab.fr/>

__Site de Planète Sciences :__ <http://www.planete-sciences.org/national/>

# Fonctionnement du module

Le script bash __start.sh__ lance successivement les sripts python __Read.py__ et __Send.py__.

__Read.py__ attend le passage d'un badge sur le lecteur et écrit l'identifiant unique de ce badge dans le fichier __idfile.txt__. Ensuite, __Send.py__ lit lidentifiant écrit dans ce fichier et l'envoie dans une trame TCP sur le réseau pour réception par une application tierce.

# Installation du module

## Installer les bibiliothèques nécéssaires

Le module Plascilab-RPi-RFID utilise plusieurs bibliothèques pour fonctionner :

* __spidev__, pour gérer l'interface SPI ;
* __MFRC522__, pour gérer le lecteur RFID.

Pour installer ces deux bibliothèques, ouvrez un terminal sur le Raspberry PI (_via_ une session SSH ou directement en branchant un clavier et un écran au Raspberry) et entrez les deux commandes suivantes :

`sudo pip3 install spidev`

`sudo pip3 install mfrc522`

## Activer l'interface SPI

L'interface SPI permet de communiquer avec le lecteur RFID. Pour l'activer, ouvrez un terminal sur le Raspberry et entrez dans la configuration de la carte en tapant `sudo raspi-config`. Avec les touches du clavier, navigez vers __"5 Interfacing Options"__. Tapez sur __Entrée__ puis sélectionnez __"P4 SPI"__. Répondez __"Yes"__ lorsque l'outil de configuration vous demande de confirmer l'activation de l'interface SPI. Une fois l'option activée, quittez l'outil de configuration en appuyant autant de fois que nécéssaire sur la touche __"Échap"__ afin de retourner au terminal.

Il reste enfin à redémarrer le Raspberry PI en tapant la commande `sudo reboot now`.

## Télécharger et installer le module

Pour télécharger le module, cliquez sur le bouton "Clone or download" puis sur "Download ZIP".

Extrayez ensuite le fichier où vous le souhaitez. Copiez le contenu du dossier `pi-rfid` sur le Raspberry PI _via_ une session SSH ou directement en mode graphique.

Naviguez ensuite à l'intérieur de ce dossier et tapez la commande `chmod +x start.sh` pour autoriser l'éxécution du fichier __start.sh__.

Si vous souhaitez que le programme de détection de badge démarre au démarrage du Raspberry, il est possible de créer un tâche de démarrage grâce à la table de planification __crontab__. Pour ce faire, entrez la commande suivante :

`sudo crontab -e`

Si crontab vous demande de choisir un éditeur, sélectionnez l'option __1 nano__. Un éditeur de texte s'ouvre alors. Déplacez votre curseur avec les touches du clavier en bas du fichier et ajoutez la ligne suivante :

`@reboot (sudo sleep 40 ; sudo <chemin>/pi-rfid/start.sh) &` où `<chemin>` est le chemin de dossiers contenant `pi-rfid`.

Entrez ensuite la combianaison de touches __CTRL+O__ pour suavegarder, puis tapez sur __Entrée__ et enfin tapez __CTRL+X__ pour quitter l'éditeur. Le programme devrait alors se lancer au prochain démarrage.

Pour le lancer manuellement, naviguez simplement dans le dossier __pi-rfid__ et entrez la commande `sudo ./start.sh`.

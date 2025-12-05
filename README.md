# Projet Banc d'essai - IPSA Rocket

Ce projet développe un banc d'acquisition de données pour tracer les courbes de poussée de moteurs de rocketry amateur. Objectifs : analyser la fiabilité des moteurs et présenter nos travaux aux futurs étudiants d'IPSA.

## Environnement de développement

- IDE recommandé : **Visual Studio Code (VSCode)**
- Extension VSCode : **MicroPico**
- Capteur : **HX711** https://github.com/robert-hh/hx711.git (librairie `hx711_gpio.py` incluse dans le projet, licence MIT d’origine conservée)

## Installation et configuration

1. Créez un répertoire pour le projet.
2. Clonez la librairie Fast_hx711 utilisée pour la lecture du capteur de force HX711 :
   ```
   git clone https://github.com/STARdevgroup/Fast_hx711.git
   ```
3. Accédez au dossier `Fast_hx711` dans le répertoire créé.
4. Installez l'extension **MicroPico** dans VSCode.
5. Ouvrez la palette de commandes (Ctrl+Shift+P ou barre de recherche) et lancez :
   ```
   MicroPico: Initialize MicroPico Project
   ```
6. Préparez le Raspberry Pi Pico pour le flashage : maintenez le bouton **BOOTSEL** enfoncé et branchez-le à l’ordinateur. Le Pico doit apparaître comme un disque externe nommé `RPI-RP2`.
7. Téléchargez le firmware MicroPython UF2 pour Pico depuis :
   [https://micropython.org/download/RPI_PICO_W/](https://micropython.org/download/RPI_PICO_W/)
8. Glissez déposez le fichier UF2 sur le disque `RPI-RP2`. Le Pico redémarrera automatiquement.
9. Pour déployer le code, sélectionnez dans VSCode les fichiers `main.py` et `hx711_gpio.py`, faites un clic droit et choisissez :
   ```
   Upload Project to Pico
   ```

Votre environnement est prêt à fonctionner avec le banc d’essai et la librairie Fast_hx711 pour la gestion du capteur HX711.  

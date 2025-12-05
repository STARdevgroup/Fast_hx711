```markdown
# Projet Banc d’essai – IPSA Rocket

Ce projet réalise un banc d’acquisition de données pour tracer les courbes de poussée de moteurs de rocketry amateur.  
Objectifs : analyser la fiabilité des moteurs et présenter nos travaux aux futurs étudiants de l’IPSA.

## Environnement de développement

- IDE recommandé : **Visual Studio Code (VSCode)**
- Extension VSCode : **MicroPico**
- Carte cible : **Raspberry Pi Pico W**
- Capteur : **HX711** (librairie `hx711_gpio.py` incluse dans le projet, licence MIT d’origine conservée)

## Installation et configuration

1. Clonez le projet :
   ```
   git clone https://github.com/STARdevgroup/Fast_hx711.git
   cd Fast_hx711
   ```

2. Ouvrez le dossier dans **VSCode**.

3. Installez l’extension **MicroPico** puis ouvrez la palette de commandes (`Ctrl+Shift+P`) et lancez :
   ```
   MicroPico: Initialize MicroPico Project
   ```

## Flashage du Raspberry Pi Pico W

1. Maintenez le bouton **BOOTSEL** du Pico enfoncé et branchez-le en USB.
2. Le Pico doit apparaître comme un disque externe nommé **RPI-RP2**.
3. Téléchargez le firmware MicroPython UF2 pour Pico W :  
   https://micropython.org/download/RPI_PICO_W/
4. Glissez–déposez le fichier `.uf2` sur le disque **RPI-RP2**.  
   Le Pico redémarre automatiquement avec MicroPython.

## Déploiement du code

1. Dans VSCode, sélectionnez `main.py` et `hx711_gpio.py`.
2. Clic droit → **Upload Project to Pico** (commande MicroPico).
3. Le code est maintenant sur la carte et prêt à être exécuté.

L’environnement est désormais opérationnel pour utiliser le banc d’essai et enregistrer les courbes de poussée avec le capteur HX711.
``` 

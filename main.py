from machine import Pin
from hx711_gpio import HX711
# main.py
import time 
from data import log_usb,get_log

log = get_log()
file_name = f"data_log_{log}.csv"

# Broches du Pico
DATA_PIN = 19   # DOUT du HX711
CLOCK_PIN = 18  # PD_SCK du HX711

# Instance du capteur (ordre: clock, data)
hx711 = HX711(Pin(CLOCK_PIN, Pin.OUT), Pin(DATA_PIN, Pin.IN, pull=Pin.PULL_DOWN))

# Tare (compense le poids du plateau)
hx711.tare()

# Facteur d'échelle (à calibrer avec une masse connue)
scale_factor = 1/725 * 9.81 
seuil = 0.2

tare_time = 10000
before_time_tare = time.ticks_ms()
tare_value = []
while time.ticks_diff(time.ticks_ms(), before_time_tare) < tare_time:
    raw = hx711.read()          # lecture brute (24 bits signés)
    weight = raw * scale_factor # conversion en grammes
    tare_value.append(weight)
tare_value = sum(tare_value) / len(tare_value)
    
while True:
    raw = hx711.read()          # lecture brute (24 bits signés)
    weight = raw * scale_factor - tare_value# conversion en grammes
    if weight > seuil:
        log_usb(weight,path = file_name)
    print(f"{weight:6.1f} g", end="\r")

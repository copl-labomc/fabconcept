from pyfirmata import Arduino, util
import time

# Configuration des paramètres de connexion
port = 'COM4'  # Remplacez cela par le port approprié
board = Arduino(port, )

# Broches utilisées pour le stepper motor
coil_pins = [8, 9, 10, 11]  # Broches pour les bobines du stepper motor

# Configuration des broches en tant que sortie
for pin in coil_pins:
    board.digital[pin].mode = board.get_pin('d:{}:o'.format(pin)).mode

# Séquences de bobinage pour le stepper motor
full_step_sequence = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
]
full_step_sequence = [
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

# Fonction pour faire avancer le stepper motor d'un pas
def step_forward():
    for step in full_step_sequence:
        for pin, state in zip(coil_pins, step):
            board.digital[pin].write(state)
        time.sleep(0.2)  # Ajoutez un délai pour contrôler la vitesse du stepper motor

# Fonction pour faire reculer le stepper motor d'un pas
def step_backward():
    for step in reversed(full_step_sequence):
        for pin, state in zip(coil_pins, step):
            board.digital[pin].write(state)
        time.sleep(0.05)  # Ajoutez un délai pour contrôler la vitesse du stepper motor

try:
    while True:
        # Faites avancer le stepper motor
        step_forward()
        # time.sleep(0.001)  # Attendre 0.5 seconde avant de faire reculer
        # # Faites reculer le stepper motor
        # step_backward()
        # time.sleep(0.5)  # Attendre 0.5 seconde avant de faire avancer à nouveau

except KeyboardInterrupt:
    # Fermeture de la connexion avec Arduino
    board.exit()

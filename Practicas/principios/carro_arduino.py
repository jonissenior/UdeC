from l293d import L293D
import time

# Configura los pines GPIO según tu conexión
motor = L293D(17, 4, 24, 23)  # Pines: IN1, IN2, IN3, IN4

try:
    while True:
        # Gira el motor en una dirección
        motor.clockwise()
        time.sleep(2)

        # Detiene el motor
        motor.stop()
        time.sleep(1)

        # Gira el motor en la dirección opuesta
        motor.anticlockwise()
        time.sleep(2)

        # Detiene el motor nuevamente
        motor.stop()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nDeteniendo el motor.")
    motor.stop()


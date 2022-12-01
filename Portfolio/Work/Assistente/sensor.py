import time

import RPi.GPIO as GPIO


def sensor():
    """configuração do sensor de ultra som
    """
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO_ECHO = 7
        GPIO_TRIG = 11

        GPIO.setup(GPIO_TRIG, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

        GPIO.output(GPIO_TRIG, GPIO.LOW)

        print("Aguardando o sensor estabilizar")

        time.sleep(2)

        print("Calculo da distância")

        GPIO.output(GPIO_TRIG, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(GPIO_TRIG, GPIO.LOW)

        while GPIO.input(GPIO_ECHO) == 0:
            pulse_start_time = time.time()
            while GPIO.input(GPIO_ECHO) == 1:
                pulse_end_time = time.time()

                pulse_duration = pulse_end_time - pulse_start_time

                distance = round(pulse_duration * 17150, 2)

                print("Distância: ", distance, " em cm")
                return distance
    finally:
        GPIO.cleanup()
        pass


if __name__ == '__main__':
    sensor()

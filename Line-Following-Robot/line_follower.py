import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


AIN1 = 23
AIN2 = 24
PWMA = 18

BIN1 = 27
BIN2 = 22
PWMB = 13

STBY = 25


LEFT_SENSOR = 5
RIGHT_SENSOR = 6


speed = 70
turnspeed = 50

motor_pins = [AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY]

for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)

GPIO.setup(LEFT_SENSOR, GPIO.IN)
GPIO.setup(RIGHT_SENSOR, GPIO.IN)

GPIO.output(STBY, GPIO.HIGH)


left_pwm = GPIO.PWM(PWMA, 1000)
right_pwm = GPIO.PWM(PWMB, 1000)

left_pwm.start(0)
right_pwm.start(0)



def forward():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)

    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)

    left_pwm.ChangeDutyCycle(speed)
    right_pwm.ChangeDutyCycle(speed)


def left():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)

    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)

    left_pwm.ChangeDutyCycle(0)
    right_pwm.ChangeDutyCycle(turnspeed)


def right():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)

    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)

    left_pwm.ChangeDutyCycle(turnspeed)
    right_pwm.ChangeDutyCycle(0)


def stop():
    left_pwm.ChangeDutyCycle(0)
    right_pwm.ChangeDutyCycle(0)




try:
    while True:
        left_sensor = GPIO.input(LEFT_SENSOR)
        right_sensor = GPIO.input(RIGHT_SENSOR)

        print("Sol:", left_sensor, "Sağ:", right_sensor)

        if left_sensor == 0 and right_sensor == 0:
            forward()

        elif left_sensor == 0 and right_sensor == 1:
            left()

        elif left_sensor == 1 and right_sensor == 0:
            right()

        else:
            stop()
        

        time.sleep(0.02)

except KeyboardInterrupt:
    stop()
    left_pwm.stop()
    right_pwm.stop()
    GPIO.output(STBY, GPIO.LOW)
    GPIO.cleanup()

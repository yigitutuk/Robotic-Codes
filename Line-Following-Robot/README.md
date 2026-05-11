PWM-Controlled Line Following Robot

This project implements a line-following robot using sensor feedback and PWM motor control. The robot detects the line using sensors and adjusts wheel speed during turning conditions.

Tools Used
Python
GPIO BCM pins
PWM control
Infrared sensors
Time module
How It Works

The required libraries are first imported and GPIO pins are configured as input/output. Movement functions such as left, right, and stop are defined. Inside the main loop, the robot reads sensor signals and decides the direction accordingly.

Challenges

The main challenge was implementing PWM logic and translating motor speed control into code.

Future Improvements

A PID controller could be added for smoother and more accurate line tracking.

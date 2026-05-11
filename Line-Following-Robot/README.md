

This project implements a line-following robot using sensor feedback and PWM motor control. The robot detects the line using sensors and adjusts wheel speed during turning conditions.Firstly, the required libraries were imported and GPIO pins were configured as input/output. After that movement functions such as left, right, and stop were defined. Inside the main loop, the robot reads sensor signals and decides the direction accordingly. The main challenge in this project was implementing PWM logic and translating motor speed control into code. For future improvements, a PID controller could be added for smoother and more accurate line tracking.

Tools Used:

Python,
GPIO BCM pins,
PWM control,
Infrared sensors,
Time module








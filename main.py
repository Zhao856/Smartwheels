import pygame
from controller import Controller
from softnet import Client
import time
# pygame.init()
# pygame.joystick.init()

# joystick = pygame.joystick.Joystick(0)
# joystick.init()

# while True:
#     pygame.event.pump()  # Needed to update internal state
#     x_axis = joystick.get_axis(2)  # Left stick horizontal
#     y_axis = joystick.get_axis(3)  # Left stick vertical
#     print(f"X: {x_axis:.2f}, Y: {y_axis:.2f}")

control = Controller()
client = Client("192.168.0.111",50007)
time.sleep(5)


while True:
    print(control.dic["RAnalog"])
    print(control.dic["LAnalog"])
    client.send(control.dic)

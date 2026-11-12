import pygame
from controller import Controller
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

while True:
    print(control.dic["RAnalog"])
    print(control.dic["LAnalog"])

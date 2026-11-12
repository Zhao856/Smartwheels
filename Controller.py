#reading inputs from the controller

import inputs
import threading
import pygame

class Controller:
    def __init__(self):
        self.device = inputs.devices
        self.dic = {"RAnalog": 0.0,"LAnalog":0.0}
        self.thread = threading.Thread(target = self.__return_controller)
        self.thread.daemon = True
        self.thread.start()
    def __return_controller(self):
        pygame.init()
        pygame.joystick.init()

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        while True:
            pygame.event.pump()  # Needed to update internal state
            self.dic["LAnalog"] = -1*round(joystick.get_axis(1),2)  # Left stick horizontal
            self.dic["RAnalog"] = round(joystick.get_axis(2),2)  # Left stick vertical



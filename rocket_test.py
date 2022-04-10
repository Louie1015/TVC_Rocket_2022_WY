# this is a rocket flight simulation for model rockets

# imports and libraries
import numpy as np
#import matplotlib
import turtle
import time

# params n stuff
TIMER = 0
TIME_STEP = 0.005
SETPOINT = 10
SIM_TIME = 10 #
INITIAL_X = 0
INITIAL_Y = -100
MASS = 1 #kg bc fuc imperial
MAX_THRUST = 15 #newtons
g = -9.81 #gravity
V_i = 0 #velocity
Y_i = 0 #height
BURNTIME = 1.7 #seconds
#-------------------------
KP = 1.0
KI = 0.0
KD = 1.0




class Simulation(object):
    def __init__(self):
        self.Insight = Rocket()
        self.pid = PID(KP,KI,KD,SETPOINT)
        self.screen = turtle.Screen()
        self.screen.setup(1280,900)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(15,SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
    def cycle(self):
        while self.sim:
        #get a thrust output from our PID
            thrust = self.pid.compute(self.Inisght.get_y())
            print(thrust)
            self.Insight.set_ddy(thrust)
            self.insight.set_dy()
            self.Insight.set_y()
            time.sleep(TIME_STEP)
            self.timer += 1
            if self.timer > SIM_TIME:
                    print ("SIM OVER")
                    self.sim = False
            elif self.Inisght.get_y() > 800:
                    print ("OUT OF BOUNDS")
                    self.sim = False
            elif self.Inisght.get_y() < -800:
                    print("OUT OF BOUNDS")
                    self.sim = False


class Rocket(object):
    def __init__(self):
        global Rocket
        self.Rocket = turtle.Turtle()
        self.Rocket.shape('square')
        self.Rocket.color('black')
        self.Rocket.goto(INITIAL_X,INITIAL_Y)
        self.Rocket.speed(0)
        #math vvv
        self.ddy = 0
        self.dy = V_i
        self.y = INITIAL_Y
    def set_ddy(self,thrust):
        self.ddy = g + thrust / MASS
    def get_ddy(self):
        return self.ddy
    def set_dy(self):
        self.dy += self.ddy
    def get_dy(self):
        return self.dy
    def set_y(self):
        rocket.sety(self.y + self.dy)
    def get_y (self):
        self.y = rocket.ycor()
        return self.y
class PID(object):
    def __init__(self,KP,KI,KD,target):
        self.kp = KP
        self.ki = KI
        self.KD = KD
        self.setpoint = target
        self.error  = 0
        self.integral_error = 0
        self.error_last = 0
        self.derivative_error = 0
        self.output = 0
    def compute(self, pos):
        self.error = target - pos
        self.integral_error += self.error * TIME_STEP
        self.derivative_error = (self.error - self.error_last) / TIME_STEP
        self.error_last  =self.error
        self.output = self.kp*self.error + self.ki*self.integral_error + self.kd*self.derivative_error
        if self.output >= MAX_THRUST:
            self.output = MAX_THRUST
        elif self.output <= 0:
            self.output = 0
        return self.output


def main():
    sim = Simulation()
    sim.cycle()

main()

"""
while TIMER <= BURNTIME: #Physics, takes values to calculate first position after rocket motor burns, then
    total_force = (MAX_THRUST-(MASS*gravity))
    acceleration = total_force/MASS
    V_i = acceleration * TIMER
    position = V_i * TIMER
while TIMER > BURNTIME:
    acceleration = -V_i / (TIMER - BURNTIME)
    velocity2 = V_i + (acceleration * TIMER)
    position2 = position + (velocity2 * TIMER)
"""
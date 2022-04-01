# this is a rocket flight simulation for model rockets

# imports and libraries
import numpy as np
import matplotlib
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



class Simulation(object):
    def __init__(self):
        self.Insight = Rocket()
        self.screen = turtle.Screen()
        self.screen.setup(1280,900)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(90)
        self.marker.goto(15,SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
    def cycle(self):
        while self.sim:
        #get a thrust output from our PID
            thrust = 5
            self.Insight.set_ddy(thrust)
            self.insight.set_dy()
            self.Insight.set_y()
            time.sleep(TIME_STEP)
            self.timer += 1
            if self.timer > SIM_TIME:
                    self.sim = False
            elif self.Inisght.get_y() > 800:
                    self.sim = False
            elif self.Inisght.get_y() < -800:
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


def main():
    sim = Simulation()
    sim.cycle()
    
while TIMER <= BURNTIME: #Physics, takes values to calculate first position after rocket motor burns, then 
    total_force = (MAX_THRUST-(MASS*gravity))
    acceleration = total_force/MASS
    velocity = acceleration * TIMER
    position = velocity * TIMER
while TIMER > BURNTIME:
    acceleration = -(velocity)/(TIMER - BURNTIME)
    velocity2 = velocity + (acceleration * TIMER)
    position2 = position + (velocity2 * TIMER)

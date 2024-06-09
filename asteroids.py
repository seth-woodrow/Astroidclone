import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("AstroidClone")
wn.setup(800, 600)
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)

class Sprite():
    def __init__(self):
        self.x =0
        self.y =0
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "white"
        self.size = 1.0
        self.avtive = True

    def update(self):
        if self.avtive:
            self.x += self. dx
            self.y += self.dy
            
            if self.x > 400:
                self.x =-400
            elif self.x <-400:
                self.x = 400

            if self.y > 300:
                self.y = -300
            elif self.y < -300:
                self.y  = 300

    def render(self, pen):
        if self.avtive:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size, self.size, 0)
            pen.color(self.color)
            pen.stamp()

    def is_collision(self, other):
        x = self.x-other.x
        y = self.y-other.y
        distance = ((x**2)+(y**2))**0.5
        if distance < ((10*self.size)+(10*other.size)):
            return True
        else:
            return False
        
    def goto(self, x, y):
        self.x = x
        self.y = y


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "triangle"
        self.lives = 3
        self.score = 0

        def rotate_left(self):
            self.heading += 30

        def rotate_right(self):
            self.heading -= 30

        def accelerate(self):
            ax = math.cos(math.radians(self.heading))
            ay = math.sin(math.radians(self.heading))
            self.dx += ax * 0.1
            self.dy += ay * 0.1

        def render(self, pen):
            if self.active:
                pen.goto(self.x, self.y)
                pen.setheading(self.heading)
                pen.shape(self.shape)
                pen.shapesize(self.size/2.0, self.size, 0)
                pen.color(self.color)
                pen.stamp()

class Asteroid(Sprite):
    def __init__(self):
        Sprite().__init__(self)
        self.shape = "circle"
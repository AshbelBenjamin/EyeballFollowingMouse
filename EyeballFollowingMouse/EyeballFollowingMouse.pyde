from math import sin

X = 30
Y = 30
delay = 16
radius = 30

def setup():
    strokeWeight(7)
    frameRate(20)
    size(500,500)

def draw():
    global X, Y, radius
    background(100)
    fill(0,121,184)
    stroke(255)
    fc = frameCount

    X += (mouseX-X)/delay;
    Y += (mouseY-Y)/delay;

    radius = radius + sin(fc / 4)

    ellipse(X,Y,radius,radius)

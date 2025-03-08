import math
from turtle import *

def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(9000)
bgcolor("black")
color("red")

penup()
begin_fill() # filling shape color

for k in range(0, 628):  # Use 0 to 2*pi (0 to 628 for integer k)
    x = hearta(k / 100) * 20
    y = heartb(k / 100) * 20
    goto(x,y)
pendown()
end_fill()
done()

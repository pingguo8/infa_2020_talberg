#Тальберг Е. Б02-010

import turtle

turtle.speed(5)

x = 0
y = 0

vx = 20
vy = 50
a = -10

dt = 0.1
for i in range(200):
    x += vx * dt
    vy += a * dt
    y += vy * dt + a * dt * dt / 2
    turtle.goto(x, y)
    if y <= 0:
        vy *= -1
        y = 0
        
turtle.done()

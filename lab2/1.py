#Тальберг Е. Б02-010

import turtle
from random import *

turtle.shape('turtle')


for i in range(50):
    turtle.forward(randint(0, 100))
    turtle.left(randint(0, 90))
    
turtle.done()

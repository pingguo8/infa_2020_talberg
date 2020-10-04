#Тальберг Е. Б02-010

import turtle

a = 20
turtle.shape('turtle')


number_0 = [(a, 90), (2*a, 90)]
number_1 = [(90, 2*a), (135, a), (225, a)]
number_4 = [(2*a, a), (90, a)]
number_7 = [(90, a), (45, a), (180, a)]

def number_00():
    turtle.pendown()
    for i in range(2):
        turtle.forward(number_0[0][0])
        turtle.left(number_0[0][1])
        turtle.forward(number_0[1][0])
        turtle.left(number_0[1][1])
    turtle.penup()
 

def number_01():
    turtle.pendown()
    turtle.left(number_1[0][0])
    turtle.forward(number_1[0][1])
    turtle.left(number_1[1][0])
    turtle.forward(number_1[1][1])
    turtle.right(number_1[2][0])
    turtle.penup()
    

def number_04():
    turtle.penup()
    turtle.forward(number_4[0][1])
    turtle.pendown()
    turtle.left(number_4[1][0])
    turtle.forward(number_4[0][0])
    turtle.backward(number_4[0][1])
    turtle.left(number_4[1][0])
    turtle.forward(number_4[1][1])
    turtle.right(number_4[1][0])
    turtle.forward(number_4[1][1])
    turtle.right(number_4[1][0])
    turtle.penup()
    
def number_07():
    turtle.pendown()
    turtle.left(number_7[0][0])
    turtle.forward(number_7[0][1])
    turtle.right(number_7[1][0])
    turtle.forward(number_7[1][1])
    turtle.left(number_7[1][0])
    turtle.forward(number_7[1][1])
    turtle.left(number_7[0][0])
    turtle.forward(number_7[0][1])
    turtle.penup()
    turtle.right(number_7[2][0])


number_01()
turtle.goto(2*a, 0)
number_04()
turtle.goto(5*a, 0)
number_01()
turtle.goto(7*a, 0)
number_07()
turtle.goto(9*a, 0)
number_00()
turtle.goto(11*a, 0)
number_00()


turtle.done()

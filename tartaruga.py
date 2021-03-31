from turtle import *

pen = Turtle()
window = Screen()

lung = 50
pen.home()

def controllo():
    if (pen.ycor() + lung) > window.window_height()/2:
        return 1
    elif (pen.ycor() - lung) < -1 * window.window_height() / 2: 
        return 2
    elif (pen.xcor() + lung) > window.window_width()/2:
        return 3
    elif (pen.xcor() - lung) < -1 * window.window_width() / 2:
        return 4
    else:
        return 0

def avanti():
    if controllo() != 1: 
        pen.setheading(90)
        pen.forward(lung)
        print(controllo())
    else:
        pass

def indietro():
    if controllo() != 2: 
        pen.setheading(270)
        pen.forward(lung)
        print(controllo())
    else:
        pass

def sinistra():
    if controllo() != 4: 
        pen.setheading(180)
        pen.forward(lung)
        print(controllo())
    else:
        pass

def destra():
    if controllo() != 3: 
        pen.setheading(0)
        pen.forward(lung) 
        print(controllo())
    else:
        pass

window.title("turtle")

window.listen()
window.onkeypress(avanti, "w")
window.onkeypress(destra, "d")
window.onkeypress(sinistra, "a")
window.onkeypress(indietro, "s")

window.mainloop()
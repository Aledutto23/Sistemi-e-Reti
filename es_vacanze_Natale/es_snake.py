import turtle
import time
import random

delay = 0.1

#dichiaro le variabili del punteggio
Punteggio = 0
punt_max = 0

#inserisco le impostazioni dello schermo
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) 

#impostazioni della testa dello snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#impostazioni per il cibo dello snake
cibo = turtle.Turtle()
cibo.speed(0)
cibo.shape("circle")
cibo.color("red")
cibo.penup()
cibo.goto(0,100)

segmenti = []

#impostazioni per il disegno
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Punteggio: 0  Punteggio Massimo: 0", align="center", font=("Courier", 20, "normal"))

#funzioni per il movimento dello snake
def alto():
    if head.direction != "down":
        head.direction = "up"

def basso():
    if head.direction != "up":
        head.direction = "down"

def sinistra():
    if head.direction != "right":
        head.direction = "left"

def destra():
    if head.direction != "left":
        head.direction = "right"

def movimento():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#impostazioni dei comandi della tastiera
wn.listen()
wn.onkeypress(alto, "w")
wn.onkeypress(basso, "s")
wn.onkeypress(sinistra, "a")
wn.onkeypress(destra, "d")

while True:
    wn.update()

    #impostazioni di controllo del bordo e delle collisioni con esso
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #nascondo i segmenti
        for segment in segmenti:
            segment.goto(1000, 1000)
        
        #azzerare i segmenti
        segmenti.clear()

        #imposto il punteggio a 0
        Punteggio = 0

        #reimpostare il delay
        delay = 0.1

        pen.clear()
        pen.write("Punteggio: {}  Punteggio Massimo: {}".format(Punteggio, punt_max), align="center", font=("Courier", 20, "normal")) 


    #impostazione dello snake quando tocca il cibo
    if head.distance(cibo) < 20:
        #impostazione per il movimento casuale del cibo
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        cibo.goto(x,y)

        #impostazione per aggiungere un segmento
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segmenti.append(new_segment)
        delay -= 0.001

        #incrementare il punteggio
        Punteggio += 1

        if Punteggio > punt_max:
            punt_max = Punteggio
        
        pen.clear()
        pen.write("Punteggio: {}   Punteggio Massimo: {}".format(Punteggio, punt_max), align="center", font=("Courier", 20, "normal")) 

    #impostazione per muovare gli ultimi segmanti in testa
    for index in range(len(segmenti)-1, 0, -1):
        x = segmenti[index-1].xcor()
        y = segmenti[index-1].ycor()
        segmenti[index].goto(x, y)
    if len(segmenti) > 0:
        x = head.xcor()
        y = head.ycor()
        segmenti[0].goto(x,y)

    movimento()    

    #impostazione per la collisione della testa con i segmenti del corpo
    for segment in segmenti:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            #impostazione per togliere i segmenti
            for segment in segmenti:
                segment.goto(1000, 1000)
        
            #annullare i segmenti
            segmenti.clear()

            #reimpostare il punteggio
            Punteggio = 0

            #reimpostare il delay
            delay = 0.1
        
            #impostazione per aggiornare il punteggio sullo schermo
            pen.clear()
            pen.write("Punteggio: {}  Punteggio Massimo: {}".format(Punteggio, punt_max), align="center", font=("Courier", 20, "normal"))

    time.sleep(delay)

wn.mainloop()
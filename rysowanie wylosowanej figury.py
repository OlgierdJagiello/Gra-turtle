import turtle
import random
from time import time
a=0
b=1
def tablica_wynik(tab):
    if len(tab)==0:
        min=10000000000000
    else:
        min=float(tab[0])+1
    for i in range(len(tab)):
        if float(tab[i])<min:
            min=float(tab[i])
    return min
def czas():
    t2=time()
    czas=round(t2-t1,2)
    turtle1.penup()
    turtle1.goto(200,200)
    turtle1.pendown()
file=open("wyniki.txt","a")
    file2=open("wyniki.txt","r")
    file2=file2.read().split()
    print(file2)
    print(czas,file=file)
    if czas<tablica_wynik(file2):
        turtle1.pencolor("green")
    else:
        turtle1.pencolor("red")
    turtle1.write(f"Czas:{czas}", font=('Arial', 16, 'normal'))
def rozmiar_up():
    global b
    turtle1.pensize(b+1)

def rozmiar_down():
    turtle1.pensize(b-1)
def pen_color():
    global a
    turtle1.pencolor(colors[a])
    a+=1
    a=a%len(colors)
    return a

def zasady():
    turtle1.penup()
    turtle1.goto(-450,200)
    turtle1.write(zasady_gry,font=('Arial', 16, 'normal'))
def up():
    turtle1.fd(10)


def down():
    turtle1.fd(-10)


def left():
    turtle1.left(10)


def right():
    turtle1.right(10)


def reset():
    turtle1.setheading(0)
    turtle1.pencolor("black")
    turtle1.penup()
    turtle1.goto(0, 0)
    turtle1.pendown()


def losowanie_figury():
    figury = [kwadrat, prostokąt, trójkąt_rówb, pięciokąt, dziesięciokąt]
    turtle1.penup()
    turtle1.goto(0, 165)
    turtle1.pendown()
    random.choice(figury)()
    reset()


def reset_window():
    turtle1.clear()
    reset()


def kwadrat():
    for i in range(4):
        turtle1.forward(100)
        turtle1.left(90)


def prostokąt():
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(50)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(50)


def trójkąt_rówb():
    for i in range(3):
        turtle1.forward(100)
        turtle1.left(120)


def pięciokąt():
    for i in range(5):
        turtle1.forward(100)
        turtle1.left(72)


def dziesięciokąt():
    for i in range(10):
        turtle1.forward(50)
        turtle1.left(36)

colors=["black","grey","white","red","yellow","orange","pink","purple","blue","green"]
zasady_gry="""Hej witaj w mojej grze
Twoim zadaniem jest odrysować figurę narysowaną na ekranie w jak najmniejszym czasie.
Poruszasz się strzałkami.
Gdy skończysz kliknij SPACE aby zobaczyć swoj czas.
Jeśli napis jest na zielono, to jest to twój najlepszy wynik.
A jeśli na czerwono,to nie pobiłeś swojego rekordu
Klikająć R resetujesz grę.
Aby zacząć kliknij R, potem S."""

# zmienna oznaczająca indeks w tab colors w fun pen_color
turtle1 = turtle.Turtle()
win = turtle.Screen()
win.setup(1000, 800)
win.bgcolor("palegreen")
zasady()
t1=time()



win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")
win.onkeypress(reset_window, "r")
win.onkeypress(czas,"space")
win.onkeypress(losowanie_figury,"s")
win.onkeypress(pen_color,"p")
win.onkeypress(rozmiar_up,"d")
win.onkeypress(rozmiar_down,"m")
turtle1.screen.mainloop()
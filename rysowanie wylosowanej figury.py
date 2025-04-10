import turtle
import random
from time import time

def tablica_wynik(tab):
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
def pen_color(a):
    turtle1.pencolor(colors[a])
    if a == len(colors)-1:
        a = 0
    else:
        a+=1
    return a
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
    losowanie_figury()
    # reset()


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
Klikająć R resetujesz grę."""
a=0
# zmienna oznaczająca indeks w tab colors w fun pen_color
turtle1 = turtle.Turtle()
win = turtle.Screen()
win.setup(1000, 800)

losowanie_figury()
t1=time()

win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")
win.onkeypress(reset_window, "r")
win.onkeypress(czas,"space")
win.onkeypress(pen_color(a),"p")
turtle1.screen.mainloop()
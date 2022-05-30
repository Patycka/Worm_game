# # Obsługa klawiatury - początek

'''
Tworzenie listy
https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

'''

from math import sqrt
from turtle import*
# View -> Tool windows -> Python Packages (pygame installation in pycharm) or pip install pygame in VS
import random
import time

pressed_key = ""
rozmiar_planszy = 20
X = -300
Y = 300
BOK = abs(X) + abs(Y)
czas_odswiezania = 1
liczba_kamieni = 3
liczba_pol_z_jedzeniem = 2
margx = 20
margy = 50
odstep = int(BOK / rozmiar_planszy)

# Closure (funkcja anonimowa)
def set_direction(key):
    def result():
        global pressed_key
        pressed_key = key
        print(f'The key was pressed')
    return result

def ini_keyboard():
    tracer(0,0)

    plansza = []
    worm_list = []

    fill_board_list(plansza)

    create_board()
    list_food = []
    list_kamienie = []
    worm = Turtle()
    add_elements(list_food, list_kamienie, plansza)
    add_single_square(worm, "orange")
    add_worm_cor(worm, worm_list)

    update()
    for direction in ["", "Up", "Left", "Right", "Down", "q"]:
        onkey(set_direction(direction.lower()), direction)
    hideturtle()
    listen()
    while pressed_key != "q":
        move_worm(worm)
        update()
        time.sleep(0.5)
        clear()
    # zamyka okno
    bye()
    done()

def create_board():
    global margx
    global margy

    screen = Screen()
    screen.bgcolor("grey")
    screen.setup(BOK+margx, BOK+margy)
    screen.title("Dżdżownica")

    global rozmiar_planszy
    pen = Turtle()

    current_score()

    for a in range(rozmiar_planszy+1):
        # linie w pionie
        pen.penup()
        pen.goto(X + a*odstep, Y)
        pen.pendown()
        pen.goto(X + a*odstep, -Y)
        # linie w poziomie
        pen.penup()
        pen.goto(X, Y -a*odstep)
        pen.pendown()
        pen.goto(-X, Y -a*odstep)
    pen.hideturtle()


def add_elements(food, kamienie, plansza):
    global liczba_pol_z_jedzeniem
    global liczba_kamieni

    add_squares(food, liczba_pol_z_jedzeniem, "green", plansza)
    add_squares(kamienie, liczba_kamieni, "blue", plansza)


def add_squares(list_obj, n, color, plansza):
    for _ in range(n):
        obj = Turtle()
        list_obj.append(obj)
        add_single_square(obj, color)

def add_single_square(obj, color):
        # X powinien byc od -X do Y-1*odstep aby nie wychodzil poza kratki
        x = random.randint(X/odstep, (Y/odstep)-1)*odstep + odstep/2
        # Y powinien byc od -X+1*odstep do Y aby nie wychodzil poza kratki
        y = random.randint((X/odstep)+1, Y/odstep)*odstep - odstep/2
        obj.shape("square")
        obj.color(color)
        obj.penup()
        obj.goto(x, y)
        ilosc_kratek = rozmiar_planszy*rozmiar_planszy
        pole_kwadratu = (abs(X)*abs(Y)) / (ilosc_kratek)
        bok = sqrt(pole_kwadratu)/10
        obj.shapesize(bok, bok)
        print(obj.xcor(), obj.ycor())

def current_score(score=0):
    pen = Turtle()
    pen.penup()
    pen.goto(0, Y)
    pen.write(f'Your score is: {score}', font=10, align='center')
    pen.hideturtle()
    

def fill_board_list(plansza):
    global rozmiar_planszy
    for i in range(rozmiar_planszy):
        wiersz = []
        for _ in range(rozmiar_planszy):
            # dodawanie kolumn
            wiersz.append("p")
        plansza.append(wiersz)

def add_worm_cor(worm, worm_list):
    worm_tuple = (worm.xcor(), worm.ycor())
    worm_list.append(worm_tuple)

def move_worm(worm):
    global rozmiar_planszy
    global pressed_key
    
    if pressed_key == "up":
        y = worm.ycor()
        worm.sety(y+odstep)
    elif pressed_key == "down":
        y = worm.ycor()
        worm.sety(y-odstep)
    elif pressed_key == "left":
        x = worm.xcor()
        worm.setx(x-odstep)
    elif pressed_key == "right":
        x = worm.xcor()
        worm.setx(x+odstep)


ini_keyboard()
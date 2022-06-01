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
szerokosc_okna = 600
liczba_kamieni = 3
liczba_pol_z_jedzeniem = 2
margx = 20
margy = 50
odstep = (szerokosc_okna / rozmiar_planszy)

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
    add_single_square(worm, "orange", plansza)
    print_board_list(plansza)
    add_worm_cor(worm, worm_list)

    update()
    for direction in ["", "Up", "Left", "Right", "Down", "q"]:
        onkey(set_direction(direction.lower()), direction)
    hideturtle()
    listen()
    while pressed_key != "q":
        move_worm(worm)
        add_worm_cor(worm, worm_list)
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
    screen.setup(szerokosc_okna+margx, szerokosc_okna+margy)
    screen.title("Dżdżownica")

    global rozmiar_planszy
    pen = Turtle()

    current_score()

    # Okna ma wymiar (-szerokosc_okna/2, szerokosc_okna/2)
    a = -szerokosc_okna/2
    b = szerokosc_okna/2
    for i in range(rozmiar_planszy+1):
        # linie w pionie
        pen.penup()
        pen.goto(a + i*odstep, b)
        pen.pendown()
        pen.goto(a + i*odstep, -b)
        # linie w poziomie
        pen.penup()
        pen.goto(a, b - i*odstep)
        pen.pendown()
        pen.goto(-a, b -i*odstep)
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
        add_single_square(obj, color, plansza)

def add_single_square(obj, color, plansza):
        a = -szerokosc_okna/2
        b = szerokosc_okna/2
        index_wiersze = 0
        index_kolumny = 0
 
        # Losowanie kratek od 1 do rozmiaru planszy
        x = random.randint(1, rozmiar_planszy)
        index_kolumny = x-1          
        y = random.randint(1, rozmiar_planszy)
        index_wiersze = rozmiar_planszy - y

        # Sprawdzenie czy nie powtarza się element na danym miejscu, jeżeli tak to ponawia losowanie
        while plansza[index_wiersze][index_kolumny] == "e":
            x = random.randint(1, rozmiar_planszy)
            index_kolumny = x-1          
            y = random.randint(1, rozmiar_planszy)
            index_wiersze = rozmiar_planszy - y            

        # Zamiana kratek na współrzędne na planszy
        x = x *odstep - szerokosc_okna/2 - odstep/2
        y = y * odstep - szerokosc_okna/2 - odstep/2

        update_board_list(plansza, index_wiersze, index_kolumny)

        obj.penup()
        obj.shape("square")
        ilosc_kratek = rozmiar_planszy*rozmiar_planszy
        pole_kwadratu = (abs(a)*abs(b)) / (ilosc_kratek)
        bok = sqrt(pole_kwadratu)/10
        obj.shapesize(bok)
        obj.color(color)
        obj.goto(x, y)
        # if color == "orange":
        #     obj.stamp()
        #     obj.dot(15, 'red')

def current_score(score=0):
    pen = Turtle()
    pen.penup()
    pen.goto(0, szerokosc_okna/2)
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

def update_board_list(plansza, wiersze, kolumny):
    '''
    Aktualizuje plansze jezeli sa nowe elementy, wstawia e w miejscu elementu
    '''
    plansza[wiersze][kolumny] = "e"

def print_board_list(plansza):
    global rozmiar_planszy
    for numer_wiersza in range(rozmiar_planszy):
        print(plansza[numer_wiersza])

def add_worm_cor(worm, worm_list):
    worm_tuple = (worm.xcor(), worm.ycor())
    if worm_tuple not in worm_list:
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
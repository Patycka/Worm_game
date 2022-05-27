# # Obsługa klawiatury - początek

'''
Tworzenie listy
https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

'''

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
liczba_kamieni = 4
liczba_pol_z_jedzeniem = 3
margx = 20
margy = 50
odstep = int(BOK / rozmiar_planszy)

# Closure
def set_direction(key):
    def result():
        global pressed_key
        pressed_key = key
        print(f'The key was pressed')
    return result

def ini_keyboard():
    tracer(0,0)

    plansza = []
    global rozmiar_planszy
    worm_list = []

    fill_board_list(plansza, rozmiar_planszy)

    create_board()
    food = Turtle()
    kamienie = Turtle()
    worm = Turtle()
    add_elements(food, kamienie, worm)
    add_worm_cor(worm, worm_list)

    update()
    for direction in ["", "Up", "Left", "Right", "Down", "q"]:
        onkey(set_direction(direction.lower()), direction)
    listen()
    while pressed_key != "q":
        move_worm(worm)
        update()
        time.sleep(1)
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


def add_elements(food, kamienie, worm):
    global liczba_pol_z_jedzeniem
    global liczba_kamieni

    add_squares(food, liczba_pol_z_jedzeniem, "green")
    add_squares(kamienie, liczba_kamieni, "blue")
    add_squares(worm, 1, "orange")
    worm.direction = "Stop"


def add_squares(obj, n, color):
    for _ in range(n):

        # X powinien byc od -X do Y-1*odstep aby nie wychodzil poza kratki
        x = random.randint(X/odstep, (Y/odstep)-1)*odstep
        # Y powinien byc od -X+1*odstep do Y aby nie wychodzil poza kratki
        y = random.randint((X/odstep)+1, Y/odstep)*odstep
        obj.penup()
        obj.goto(x, y)
        obj.color(color)
        obj.begin_fill()
        # stworzenie kwadratu
        for i in range (4):
            obj.forward(odstep)
            obj.right(90)
        obj.end_fill()
        obj.hideturtle()

def current_score(score=0):
    pen = Turtle()
    pen.penup()
    pen.goto(0, Y)
    pen.write(f'Your score is: {score}', font=10, align='center')
    pen.hideturtle()
    

def fill_board_list(plansza, rozmiar):
    for i in range(rozmiar):
        wiersz = []
        for _ in range(rozmiar):
            # dodawanie kolumn
            wiersz.append(0)
        plansza.append(wiersz)

def add_worm_cor(worm, worm_list):
    worm_tuple = (worm.xcor(), worm.ycor())
    worm_list.append(worm_tuple)

def move_worm():
    print("move worm")
ini_keyboard()
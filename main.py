# # Obsługa klawiatury - początek

from turtle import*
# View -> Tool windows -> Python Packages (pygame installation in pycharm) or pip install pygame in VS
import random

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

def set_direction(key):
    def result():
        global pressed_key
        pressed_key = key
        print(f'The key was pressed')
    return result

def ini_keyboard():
    tracer(0,0)
    create_board()
    add_elements()

    update()
    for direction in ["", "Up", "Left", "Right", "Down", "q"]:
        onkey(set_direction(direction.lower()), direction)
    listen()
    done()

def create_board():
    global margx
    global margy

    screen = Screen()
    screen.bgcolor("grey")
    screen.setup(BOK+margx, BOK+margy)
    screen.title("Dżdżownica")

    global rozmiar_planszy
    odstep = int(BOK / rozmiar_planszy)
    pen = Turtle()
    pen.speed(0)
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


def add_elements():
    global liczba_pol_z_jedzeniem
    global liczba_kamieni

    food = Turtle()
    add_squares(food, liczba_pol_z_jedzeniem, "green")
    kamienie = Turtle()
    add_squares(kamienie, liczba_kamieni, "blue")
    worm = Turtle()
    add_squares(worm, 1, "orange")
    worm.direction = "Stop"


def add_squares(obj, n, color):
    odstep = int(BOK / rozmiar_planszy)
    for _ in range(n):
        obj.penup()
        # X powinien byc od -X do Y-1*odstep aby nie wychodzil poza kratki
        x = random.randint(X/odstep, (Y/odstep)-1)*odstep
        # Y powinien byc od -X+1*odstep do Y aby nie wychodzil poza kratki
        y = random.randint((X/odstep)+1, Y/odstep)*odstep
        obj.goto(x, y)
        obj.color(color)
        obj.begin_fill()
        # stworzenie kwadratu
        for i in range (4):
            obj.forward(odstep)
            obj.right(90)
        obj.end_fill()
        obj.hideturtle()

def current_score():
    pass

ini_keyboard()
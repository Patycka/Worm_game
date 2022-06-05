from math import sqrt
from operator import truediv
from turtle import*
import random
import time

# ---- Stałe ---------
rozmiar_planszy = 20
szerokosc_okna = 600
liczba_kamieni = 3
liczba_pol_z_jedzeniem = 2
margx = 20
margy = 60
odstep = (szerokosc_okna / rozmiar_planszy)


# ------------ Obsługa klawiatury - początek ----------

pressed_key = ""

def set_direction(key):
    def result():
        global pressed_key
        pressed_key = key
        print(f'The key was pressed')
    return result

def ini_keyboard():

    for direction in ["", "Up", "Left", "Right", "Down", "q"]:
        onkey(set_direction(direction.lower()), direction)
    hideturtle()
    listen()

# ----------- Obsługa klawiatury - koniec ----------



# ------------ Funkcja główna - początek ----------
def main():

    ini_keyboard()

    tracer(0,0)
    score_obj = Turtle()
    score = 0

    # Zainicjalizowanie stuktury danych, plansza (docelowo macierz) 
    # i worm_list (docelowo lista krotek współrzędnych dżdżownicy)
    plansza = []
    worm_list = []
    list_food = []
    list_kamienie = []

    # Zainicjalizowanie planszy jako listy wierszy, gdzie każdy wiersz jest listą pól.
    # Początkowo wszystkie pola są wypełnione wartościami "p" (puste)
    fill_board_list(plansza)

    # Narysowanie kratek na szarym tle
    create_board(score_obj)

    worm = Turtle()
    
    # Dodanie elementów na plansze w losowo wybranych miejscach: jedzenie, kamienie
    add_elements(list_food, list_kamienie, plansza)
    # Dodanie obiektu dżdżownica do rysunku
    add_single_square(worm, "orange", plansza)

    # Wyświetlenie zaktualizowanej struktury danych planszy, w miejscach gdzie jest element (jedzenie, kamienie)
    # jest znak "e" a na pozostałych miejscach gdzie nie ma żadnego elementu jest "p"
    print_board_list(plansza)

    # Dodanie współrzędnych dżdżownicy do listy krotek
    add_worm_cor(worm, worm_list)

    update()

    while pressed_key != "q":
        # Jeżeli dżdżownica wyjdzie poza planszę lub natrafi na kamień to koniec gry
        if is_worm_outside_board(worm) or is_worm_collide_stone(worm_list, list_kamienie):
            print_game_over()
            break
        if is_worm_eat_food(worm_list, list_food, plansza):
            score += 1
            print(score)
            current_score(score_obj, score)
        move_worm(worm)
        # Aktualizacja współrzędnych dżdżwonicy
        update_worm_cor(worm, worm_list)
        update()
        time.sleep(0.2)
        clear()

    # zamyka okno
    bye()
    done()

# ----------- Funkcja główna koniec - koniec ----------

def create_board(score_obj):
    global margx
    global margy

    screen = Screen()
    screen.bgcolor("grey")
    screen.setup(szerokosc_okna+margx, szerokosc_okna+margy)
    screen.title("Dżdżownica")

    global rozmiar_planszy
    pen = Turtle()

    current_score(score_obj, 0)

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

def current_score(obj, score):
    obj.penup()
    obj.goto(0, szerokosc_okna/2)
    obj.clear()
    obj.write(f'Your score is: {score}', font=("Arial", 12, "bold"), align='center')
    obj.penup()
    obj.goto(0, -szerokosc_okna/2-20)
    obj.write(f'Use arrows, q ends', font=("Arial", 10, "bold"), align='center')
    obj.fillcolor("blue")
    obj.hideturtle()  

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

def update_worm_cor(worm, worm_list):
    worm_tuple = (worm.xcor(), worm.ycor())
    worm_list[0] = worm_tuple

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

def is_worm_outside_board(obj):
    if (obj.xcor() > szerokosc_okna/2) or (obj.xcor() < -szerokosc_okna/2) or \
        (obj.ycor() > szerokosc_okna/2) or (obj.ycor() < -szerokosc_okna/2):
        return True
    else:
        return False

def is_worm_collide_obj(worm_list, obj_list, plansza=0, color = 0):
    for obj in obj_list:
        for worm in worm_list:
            if (worm[0] == obj.xcor()) and (worm[1] == obj.ycor()):
                if color == "green":
                    print("Add elem")
                    add_single_square(obj, color, plansza)
                return True
    return False

def is_worm_collide_stone(worm_list, stone_list):
    return is_worm_collide_obj(worm_list, stone_list)

def is_worm_eat_food(worm_list, food_list, plansza):
    return is_worm_collide_obj(worm_list, food_list, plansza, "green")

def print_game_over():
    pen = Turtle()
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.write(f'GAME OVER', font=("Arial", 20, "bold"), align='center')
    time.sleep(1)

main()
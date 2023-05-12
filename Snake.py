"""
Это игра змеика.В этом файле есть полное описание всех функции.
"""
# добавляем дополнительные библиотеки для работы с оконными приложениями, даты и времени, случайными числами.
from tkinter import *
import time
import random

# основная переменная для игры. Если она True - игра продолжается, иначе заканчивается.
Game_Running = True

# задаём размеры игрового поля, размер одной клетки змейки и её цвета.
game_width = 500
game_height = 500
snake_item = 20
snake_color1 = "green"
snake_color2 = "black"

virtual_game_x = game_width//snake_item
virtual_game_y = game_height//snake_item

snake_x = virtual_game_x//2
snake_y = virtual_game_y//2
snake_x_nav = 0
snake_y_nav = 0

# задаём начальный размер змейки
snake_list = []
snake_size = 1

# создаём окно, задаём его название
tk = Tk()
tk.title("Игра Змейка на Python")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=game_width, height=game_height,
                bd=0, highlightthickness=0)
canvas.pack()
tk.update()
# задаём цвета квадратикам и их количество
present_color1 = "red"
present_color2 = "cyan"
presents_list = []
presents_size = 20
# в рандомном порядке вывставляем квадратики на поле
for i in range(presents_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x*snake_item, y*snake_item, x*snake_item +
                             snake_item, y*snake_item+snake_item, fill=present_color2)
    id2 = canvas.create_oval(x*snake_item+2, y*snake_item+2, x*snake_item +
                             snake_item-2, y*snake_item+snake_item-2, fill=present_color1)
    presents_list.append([x, y, id1, id2])


def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(
        x*snake_item, y*snake_item, x*snake_item+snake_item, y*snake_item+snake_item, fill=snake_color2)
    id2 = canvas.create_rectangle(x*snake_item+2, y*snake_item+2, x *
                                  snake_item+snake_item-2, y*snake_item+snake_item-2, fill=snake_color1)
    snake_list.append([x, y, id1, id2])
    # print(snake_list)


snake_paint_item(canvas, snake_x, snake_y)


def check_can_we_delete_snake_item():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        # print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])


def check_if_we_found_present():
    global snake_size
    for i in range(len(presents_list)):
        if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
            # print("found!!!")
            snake_size = snake_size + 1
            canvas.delete(presents_list[i][2])
            canvas.delete(presents_list[i][3])
    #print(snake_x, snake_y)
"""
Данная функция отвечает за движение змеики влево,вправо,вверх,вниз.
"""
# функция обработки нажатий на клавиши
def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav

    if event.keysym == "w":
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == "s":
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == "a":
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == "d":
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    check_if_we_found_present()


# задаём вызов обработки нажатий на клавиши
canvas.bind_all("<KeyPress-a>", snake_move)
canvas.bind_all("<KeyPress-d>", snake_move)
canvas.bind_all("<KeyPress-w>", snake_move)
canvas.bind_all("<KeyPress-s>", snake_move)


def game_over():
    global Game_Running
    Game_Running = False

# проверяем не упёрлись ли мы в стену
def check_if_borders():
    if snake_x > virtual_game_x or snake_x < 0 or snake_y > virtual_game_y or snake_y < 0:
        game_over()


def check_we_touch_self(f_x, f_y):
    global Game_Running
    if not (snake_x_nav == 0 and snake_y_nav == 0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == f_x and snake_list[i][1] == f_y:
                Game_Running = False


# основной цикл игры
while Game_Running:
    check_can_we_delete_snake_item()
    check_if_we_found_present()
    check_if_borders()
    check_we_touch_self(snake_x + snake_x_nav, snake_y + snake_y_nav)
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.15)


# def fun_nothing(event):
#     pass


# canvas.bind_all("<KeyPress-Left>", fun_nothing)
# canvas.bind_all("<KeyPress-Right>", fun_nothing)
# canvas.bind_all("<KeyPress-Up>", fun_nothing)
# canvas.bind_all("<KeyPress-Down>", fun_nothing)


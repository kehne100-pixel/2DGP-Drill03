from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(int(x), int(y))
    delay(0.01)

def move_rectangle():
    # 아래쪽(왼->오)
    for x in range(50, 750 + 1, 5):
        draw_boy(x, 90)
    # 오른쪽(아래->위)
    for y in range(90, 550 + 1, 5):
        draw_boy(750, y)
    # 위쪽(오->왼)
    for x in range(750, 50 - 1, -5):
        draw_boy(x, 550)
    # 왼쪽(위->아래)
    for y in range(550, 90 - 1, -5):
        draw_boy(50, y)

def move_circle():
    cx, cy, r = 400, 300, 210
    for deg in range(0, 360, 2):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_boy(x, y)

def move_triangle():
    # 삼각형의 세 꼭짓점 좌표
    p1 = (400, 550)
    p2 = (750, 90)
    p3 = (50, 90)
    # p1 -> p2
    for t in range(0, 101):
        x = p1[0] + (p2[0] - p1[0]) * t / 100
        y = p1[1] + (p2[1] - p1[1]) * t / 100
        draw_boy(x, y)
    # p2 -> p3
    for t in range(0, 101):
        x = p2[0] + (p3[0] - p2[0]) * t / 100
        y = p2[1] + (p3[1] - p2[1]) * t / 100
        draw_boy(x, y)
    # p3 -> p1
    for t in range(0, 101):
        x = p3[0] + (p1[0] - p3[0]) * t / 100
        y = p3[1] + (p1[1] - p3[1]) * t / 100
        draw_boy(x, y)

while True:
    move_rectangle()
    move_circle()
    move_triangle()

close_canvas()


from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def move_top():
    print('Moving top')
    for x in range(0, 800, 30):
     draw_boy(x, 550)
    pass


def move_right():
    print('Moving right')
    for y in range(550, 50, -30):
        draw_boy(780, y)
        pass


def move_bottom():
    print('Moving bottom')
    for x in range(750, 20, -30):
        draw_boy(x, 50)
    pass



def move_left():
    print('Moving left')
    for y in range(100, 550, 30):
        draw_boy(20, y)
    pass



def move_rectangle():
    print("move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()




def move_circle():
    print("move circle")
    r = 200
    for deg in range(0, 360):
        x =  r * math.cos(math.radians(deg)) + 400
        y =  r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)



def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.01)

def move_up_diagonal():
   for x in range(0, 400, 5):
         y = x + 50
         draw_boy(x, y)
         pass




def move_down_diagonal():

    for x in range(400, 800, 5):
        y= 850 - x
        draw_boy(x, y)
        pass





def move_triangle():

    print("move triangle")
    move_up_diagonal()
    move_down_diagonal()
    move_bottom()



    pass

while True:
     move_circle()
     move_rectangle()
     move_triangle()

     pass




close_canvas()

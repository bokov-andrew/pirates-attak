import random, pgzero, pgzrun

cannon = Actor('canon', (150, 150),anchor=('left', 'center'))

def on_mouse_move(pos):
    cannon.angle = cannon.angle_to(pos)    

def draw():
    screen.clear()
    cannon.draw()

pgzrun.go()
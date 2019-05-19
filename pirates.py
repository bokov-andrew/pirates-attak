import random, pgzero, pgzrun

class Projectile(Actor):
    def __init__(self,img='cannonball',pos=(160,140),pointat=(170,130)
                 ,damage=10):
        Actor.__init__(self,img,pos)

cannonball = Projectile()

cannon = Actor('canon', (150, 150),anchor=('left', 'center'))

def on_mouse_move(pos):
    cannon.angle = cannon.angle_to(pos)    

def draw():
    screen.clear()
    cannon.draw()
    cannonball.draw()

pgzrun.go()
import random, pgzero, pgzrun
from pygame.math import Vector2

cannonball = None

class Projectile(Actor):
    def __init__(self,img='cannonball',pos=(160,140),pointat=(170,130)
                 ,damage=10):
        Actor.__init__(self,img,pos)
        print(self.pos)
        
class Cannon(Actor):
    def __init__(self,img='canon',pos=(10,140)):
        Actor.__init__(self,img,pos, anchor=('left', 'center'))
        self.length = self.width
        self.pivot = self.midleft
    def fire(self, target):
        myv=Vector2()
        myv.from_polar((self.length, self.angle))
        myv.y = - myv.y
        mypos = self.pivot + myv
        print(self.pivot)
        print(myv)
        print(self.pivot + myv)
        cannonball = Projectile(pos = mypos,pointat=target)
        return(cannonball)

cannon = Cannon()

def on_mouse_move(pos):
    cannon.angle = cannon.angle_to(pos)    

def on_mouse_down(pos):
    global cannonball
    cannonball=cannon.fire(pos)

def draw():
    screen.clear()
    cannon.draw()
    if cannonball: cannonball.draw()

pgzrun.go()
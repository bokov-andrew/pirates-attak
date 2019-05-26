import random, pgzero, pgzrun
from pygame.math import Vector2

# global variables
cannonball = None
GRAVITY=1
class Projectile(Actor):
    def __init__(self,img='cannonball',pos=(160,140),pointat=(170,130)
                 ,boost=0.1,damage=10):
        Actor.__init__(self,img,pos)
        vel = Vector2()
        vel.from_polar((self.distance_to(pointat)
               ,self.angle_to(pointat)))
        self.velocity = vel*boost
        print ('velocity:',self.velocity)
        
    def move(self):
        self.x += self.velocity.x
        self.y -= self.velocity.y
        self.velocity.y-=GRAVITY
        
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
        cannonball = Projectile(pos = mypos,pointat=target)
        return(cannonball)

cannon = Cannon()

def on_mouse_move(pos):
    cannon.angle = cannon.angle_to(pos)    

def on_mouse_down(pos):
    global cannonball
    cannonball=cannon.fire(pos)

def update():
    if cannonball: cannonball.move()

def draw():
    screen.clear()
    if cannonball: cannonball.draw()
    cannon.draw()
    
pgzrun.go()
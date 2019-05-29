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

# Let's create a new class named Base. Like the ones above, make it inherit from
# Actor like our other classes
    # define an __init__() method, with self, img, and pos as the first three
    # arguments again like above. Make a default img from the castle picture we
    # found and make up a reasonable default (x,y) tuple for the pos arguemtn.
    # Unlike above, have the following new arguments: speed,hitpoints,player
    # and make up some reasonable numeric values but player can be None
        # The body of the function should use Actor.__init__(self,img,pos)
        # Then, add a self.cannons attribute that will be an empty list
        # The self.speed, self.hitpoints, and self.player attributes should be
        # set equal the corresponding arguments
    
    # define a buyCannon method with arguments self,price,pos, and **kwargs
        # In the body, do self.cannons += [Cannon(pos,**kwargs)]
        # this adds the cannon
        # Soon, after we implement having points, we will also subtract the
        # the price of the cannon from the points the player has saved up
        # 

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
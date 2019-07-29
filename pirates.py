import random, pgzero, pgzrun
from pygame.math import Vector2

# Find/make images for the following buttons and but them into the images
# directory:
# Debug, Help, Shop, End Turn
# Later we'll reference them in this code

####################
# global variables #
####################
cannonball = None
GRAVITY=1
# Some more variables to add here (make up values for now):
# p1points, gamePhase, gameTurn, WIDTH,HEIGHT, p1activeCannon


class Projectile(Actor):
    def __init__(self,img='cannonball',pos=(60,140),pointat=(170,130)
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
    def __init__(self,img='canon',pos=(180,140)):
        Actor.__init__(self,img,pos, anchor=('left', 'center'))
        self.length = self.width
        self.pivot = self.midleft
        # add a self.state and set it to 0
    def fire(self, target):
        myv=Vector2()
        myv.from_polar((self.length, self.angle))
        myv.y = - myv.y
        mypos = self.pivot + myv
        cannonball = Projectile(pos = mypos,pointat=target)
        return(cannonball)
    
    # define one more method called click, with arguments self and mousePos
        # Return the value of self.collidepoint(mousePos)

# define a debug function, no arguments
    # In the body, just put: import pdb; pdb.set_trace()

# Let's create a new class named Base. Like the ones above, make it inherit from
# Actor like our other classes
class Base(Actor):
    # define an __init__() method, with self, img, and pos as the first three
    # arguments again like above. Make a default img from the castle picture we
    # found and make up a reasonable default (x,y) tuple for the pos arguemtn.
    # Unlike above, have the following new arguments: speed,hitpoints,player
    # and make up some reasonable numeric values but player can be None
    def __init__(self, img="castle0", pos=(10,300), speed=0, hp=60, pl=1):
        Actor.__init__(self,img,pos)
        self.cannons=[]
        self.speed=speed
        self.hp=hp
        self.pl=pl
    
    # define a buyCannon method with arguments self,price,pos, and **kwargs
        # In the body, do self.cannons += [Cannon(pos,**kwargs)]
        # this adds the cannon
        # Soon, after we implement having points, we will also subtract the
        # the price of the cannon from the points the player has saved up
        
    # define a takeDamage method with argument self, damage
        # In the body, decrease self.hitpoints by damage
        # If self.hitpoints < 0, print "Castle Destroyed"

# We're going to get rid of the line below...
cannon = Cannon()
base=Base()
# ...and replace it with base = Base()
# ...and then call the buyCannon() method of this newly created base object
# Now you'll have a base with one cannon

def on_mouse_move(pos):
    # Check that base.cannons is not empty (anymore) and if it is not empty,
    # Set the angle of base.cannons[0] to point at pos, like we're doing for
    # the test cannon below. Get rid of the line below, since we no longer have
    # a stand-alone test cannon, it's now part of a base
    cannon.angle = cannon.angle_to(pos)    

def on_mouse_down(pos):
    global cannonball
    # as above-- if base.cannons is not empty, fire base.cannons[0] instead of
    # the test cannon
    cannonball=cannon.fire(pos)

def update():
    if cannonball: cannonball.move()

def draw():
    screen.clear()
    if cannonball: cannonball.draw()
    # check that base.cannons is not empty (anymore) and if it is not, use a for
    # statement to FOO.draw() each item in base.cannons (base cannons is a list)
    # instead of drawing just this one cannon (get rid of the line below)
    cannon.draw()
    # Here also draw the base object
    base.draw()
    
pgzrun.go()
import random, pgzero, pgzrun

cannonball = None

class Projectile(Actor):
    def __init__(self,img='cannonball',pos=(160,140),pointat=(170,130)
                 ,damage=10):
        Actor.__init__(self,img,pos)
        
class Cannon(Actor):
    def __init__(self,img='canon',pos=(10,140)):
        Actor.__init__(self,img,pos, anchor=('left', 'center'))
    def fire(self, target):
        cannonball = Projectile(pos = (self.right, self.top),pointat=target)
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
from math import pow
import pygame
from pygame import sprite

class GameObject(sprite.Sprite):

    def __init__(self, image, rect, action=None):
        sprite.Sprite.__init__(self)
        self.__action = action
        self.image = image    
        self.rect = rect
                
    def update(self):
        if self.__action is not None:
            self.__action.run()
                
    def set_action(self, action):
        self.__action = action
        
        if self.__action is not None:
            self.__action.set_gameobj(self)
    
    def setxy(self, xy):
        self.rect = pygame.Rect(xy, self.rect.size)

class Action(object):
    def __init__(self, move=None, animation=None):
        self.__move = move
        self.__animation = animation 

    def set_gameobj(self, gameobj):
        self.gameobj = gameobj
    
        if self.__move is not None:
            self.__move.set_gameobj(gameobj)

        if self.__animation is not None:
            self.__animation.set_gameobj(gameobj)

    def run(self):
        if self.__animation is not None:
            self.__animation.animate(self.gameobj)
        
        if self.__move is not None:
            self.__move.move()
            
        if self.is_complete():
            self.end()
            
    def end(self):
        self.gameobj.set_action(None)
        

    def is_complete(self):
        animation = True
        move = True

        if self.__move is not None:
            move = self.__move.is_complete()
            
        if self.__animation is not None:
            animation = self.__animation.is_complete()

        return move and animation
       


class Move(object):
    def __init__(self, speed=1, frames=0, lenght=None):
        self._speed = speed
        self.__frames = frames
        self.__tick = 0
        self.__limit_len = lenght
        self.__len = 0
        self.x = 0

    def set_gameobj(self, gameobj):
        self.gameobj = gameobj

    def move(self):
        gameobj = self.gameobj
            
        if self.__tick >= self.__frames:
            self.calc()
            self.__tick = 0
            self.__len += 1
        self.__tick += 1


class Animation(object):
    def __init__(self, speed=1):
        self._speed = speed
    
    def animate(self, gameobj):
        pass

    def __init__(self, speed, frames=1, lenght=None):
        Move.__init__(self, speed, frames, lenght)

class FirstDegree(Move):
    def __init__(self, speed, frames=1, a=1, b=0, lenght=None):
        Move.__init__(self, speed, frames, lenght)
        self.__a = a
        self.__b = b

    def calc(self, x):
        return self.firstfunc(x)

    def firstfunc(self, x):
        return self.__a*x + self.__b;


class Chase(Move):
    def __init__(self, target, speed, frames=1, lenght=None):
        Move.__init__(self, speed, frames, lenght)
        self.target = target

    def calc(self):
        gameobj = self.gameobj
        gameobj.rect.x += (self.target[0] - gameobj.rect.x)/self._speed
        gameobj.rect.y += (self.target[1] - gameobj.rect.y)/self._speed

    def is_complete(self):
        
        return (self.gameobj.rect.x+self._speed, self.gameobj.rect.y+self._speed) >= self.target and False
        
class SecondDegree(Move):
    def __init__(self, speed, frames, a=1, b=0, c=0):
        Move.__init__(self, speed, frames)
        self.__a = a
        self.__b = b
        self.__c = c
        
    def calc(self, x):
        return self.secondfunc(x)

    def secondfunc(self, x):
        return self.__a*pow(x,2) + self.__b*x + self.__c+x;

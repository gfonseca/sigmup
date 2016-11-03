from math import pow
import pygame
from pygame import sprite

class GameObject(sprite.Sprite):

    def __init__(self, image, rect, action=None):
        sprite.Sprite.__init__(self)
        self.__action = action
        self.image = image    
        self.rect = rect
                
    def update():
        if action is not None:
            self.action.run(self)
    
    def set_action(self, action):
        self.__action = action
    
    def setxy(self, xy):
        self.rect = pygame.Rect(xy, self.rect.size)

class Action(object):
    def __init__(self, move=None, animation=None):
        self.__move = move
        self.__animation = animation 
    
    def run(self, gameobj):
        if self.__animation is not None:
            self.__animation.animate(gameobj)
        
        if self.__move is not None:
            self.__move.move(gameobj)
    
class Move(object):
    def __init__(self, speed=1, frames=0):
        self._speed = speed
        self._x = None;
        self.__frames = frames
        self.__tick = 0

    def move(self, gameobj):
        if self._x is None:
            self._x = gameobj.rect[0]
        
        if self.__tick >= self.__frames:
            y = self.calc(gameobj)
            gameobj.rect = pygame.Rect((self._x, y), gameobj.rect.size)
            print gameobj.rect, self._speed, self.__class__
            self._x += self._speed
            self.__tick = 0
        self.__tick += 1
        

class Animation(object):
    def __init__(self, speed=1):
        self._speed = speed
    
    def animate(self, gameobj):
        pass
        
        
class FirstDegree(Move):
    def __init__(self, speed, frames, a=1, b=0):
        Move.__init__(self, speed, frames)
        self.__a = a
        self.__b = b

    def calc(self, gameobj):
        return self.firstfunc(self._x)

    def firstfunc(self, x):
        return self.__a*self._x + self.__b;
        
class SecondDegree(Move):
    def __init__(self, speed, frames, a=1, b=0, c=0):
        Move.__init__(self, speed, frames)
        self.__a = a
        self.__b = b
        self.__c = c
        
    def calc(self, gameobj):
        return self.firstfunc(self._x)

    def firstfunc(self, x):
        return self.__a*pow(self._x,2) + self.__b*self._x + self.__c;

from math import pow
import pygame
from pygame import sprite
import operator

class GameObject(sprite.Sprite):

    def __init__(self, image, rect, action=None):
        sprite.Sprite.__init__(self)
        self.rect = rect
        self.action = action
        self.image = image
        self._pic = None

    def update(self):
        if self.action is not None:
            self.action.run()

    def set_action(self, action):
        self.action = action

        if self.action is not None:
            self.action.set_gameobj(self)

    def stop_action():
        self.action = None

    def x_methods():
        doc = "The x position of GameObject."
        def fget(self):
            return self.rect.x
        def fset(self, x):
            if type(x) is not int:
                raise AttributeError("x must be a int")
            self.rect = pygame.Rect((x, self.xy[1]), self.rect.size)
        return locals()
    x = property(**x_methods())

    def y_methods():
        doc = "The y position of GameObject."
        def fget(self):
            return self.rect.y
        def fset(self, y):
            if type(y) is not int:
                raise AttributeError("y must be a int")
            self.rect = pygame.Rect((self.xy[0], y), self.rect.size)
        return locals()
    y = property(**y_methods())

    def xy_methods():
        doc = "The xy position of GameObject."
        def fget(self):
            return (self.rect.x, self.rect.y)
        def fset(self, xy):
            if type(xy) is not tuple:
                raise AttributeError("xy must be a tuple")
            self.rect = pygame.Rect(xy, self.rect.size)
        return locals()
    xy = property(**xy_methods())

    def size_methods():
        doc = "The size of GameObject."
        def fget(self):
            return self.rect.size
        def fset(self, size):
            if type(size) is not   tuple:
                raise AttributeError("size   must be a tuple")
            self.rect = pygame.Rect(self.xy, size)
        return locals()
    size = property(**size_methods())

    def pic_methods():
        doc = "The pic position of pygame.Rect."
        def fget(self):
            return self._pic
        def fset(self, pic):
            if type(pic) is not pygame.Rect:
                raise AttributeError("pic must be a pygame.Rect")
            self._pic = pygame.Rect(pic)
        return locals()
    pic = property(**pic_methods())

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

        if self.__animation is not None:
            self.__animation.end_animation();

        if self.__move is not None:
            self.__move.end_move()

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
        self.__tick = frames
        self.__limit_len = lenght
        self.__len = 0
        self.gameobj = None

    def set_gameobj(self, gameobj):
        self.gameobj = gameobj

    def end_move(self):
        pass

    def move(self):
        if self.__tick >= self.__frames:
            self.gameobj.xy = self.calc(self.gameobj.xy)
            self.__tick = 1
            self.__len += 1
        self.__tick += 1

class Animation(object):
    def __init__(self, pics=[], frames=0, speed=1):
        self._speed = speed
        self.__pics = pics
        self.__tick = 0
        self.__frames = frames
        self.max_pics = len(pics)
        self.current_pic = 0

    def end_animation(self):
        self.current_pic = 0
        self.__tick = 0

    def set_gameobj(self, gameobj):
        self.gameobj = gameobj
        self.gameobj._pic = self.__pics[0]

    def animate(self, gameobj):
        if self.__tick >= self.__frames:
            self.gameobj._pic = self.nextPic()
            self.__tick = 0
        self.__tick += 1

    def nextPic(self):
        if self.current_pic < self.max_pics-1:
            self.current_pic += 1;
        return self.__pics[self.current_pic]

    def is_complete(self):
        return self.current_pic+1 >= self.max_pics

class FirstDegree(Move):
    def __init__(self, speed, frames=1, a=1, b=0, lenght=None):
        Move.__init__(self, speed, frames, lenght)
        self.__a = a
        self.__b = b

    def calc(self, xy):
        return self.firstfunc(xy[0])

    def firstfunc(self, x):
        return self.__a*x + self.__b;

class Chase(Move):
    def __init__(self, target, speed, frames=1, lenght=None):
        Move.__init__(self, speed, frames, lenght)
        self.target = target

    def calc(self, xy):
        x = (self.target[0] - xy[0])/self._speed
        y = (self.target[1] - xy[1])/self._speed
        return (x, y)

    def is_complete(self):
        return (self.gameobj.x+self._speed, self.gameobj.y+self._speed) >= self.target and False

class moveTo(Move):
    def __init__(self, speed=1, frames=1, direction=(0,0), lenght=None):
        Move.__init__(self, speed=speed, frames=frames, lenght=lenght)
        self.__direction = direction
        self.__complete = False

        print(self.__direction)

    def calc(self, xy):
        out_xy = tuple(map(operator.add, xy, self.__direction))
        self.__complete = True
        return out_xy

    def is_complete(self):
        return False

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

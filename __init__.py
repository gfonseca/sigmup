import os
import pygame

def init(xy, caption=None):
    pygame.init()
    screen = pygame.display.set_mode(xy)
    pygame.display.set_caption(caption)
    pygame.mouse.set_visible(0)
    return screen

def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()    


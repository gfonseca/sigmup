import core
from core import Chase
from helper import *
import pygame

screen = init((600, 600), "chimps jumping")

shp_img, shp_rect = load_image("ship2.4.png")
s = core.GameObject(shp_img, pygame.Rect(250, 500, 21, 30))
speed = 100
root_sprite = pygame.Rect(5, 1, 21, 30)
s.pic = root_sprite
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


def createGo():
    return  core.Animation(frames=20, pics=[
        root_sprite,
        pygame.Rect(38, 1, 19, 30),
        pygame.Rect(5, 33, 16, 30)]
    )

def createBack():
    return core.Animation(frames=30, pics=[
        pygame.Rect(5, 33, 16, 30),
        pygame.Rect(38, 1, 19, 30),
        root_sprite]
    )

def create_moveTo_UD(direction):
    m = None
    if(direction is not None):
        m = core.moveTo(direction)

    return core.Action(move=m, animation=None)

def create_moveTo(direction=(0,0), go=1):
    if(go):
        an = createGo()
    else:
        an = createBack()

    print(direction)
    m = core.moveTo(direction=direction)

    return core.Action(move=m, animation=an)

def create_moveTo_LR(direction, go):
    if(go):
        an = createGo()
    else:
        an = createBack()

    m = None
    if(direction is not None):
        m = core.moveTo(direction)

    return core.Action(move=m, animation=an)


def main():
    while 1:
        clock.tick(60)

        x, y = 0, 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            y = -1

        if keys[pygame.K_DOWN]:
            y = 1

        if keys[pygame.K_LEFT]:
            x = -1

        if keys[pygame.K_RIGHT]:
            x = 1

        s.set_action(create_moveTo((x,y)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        s.update()
        screen.blit(background, (0,0))
        screen.blit(s.image, s.rect, s.pic)
        pygame.display.update()
main()

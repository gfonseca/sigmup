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
    return  core.Animation(frames=30, pics=[
        root_sprite,
        pygame.Rect(38, 1, 19, 30),
        pygame.Rect(7, 34, 13, 30)]
    )


def createBack():
    return core.Animation(frames=30, pics=[
    pygame.Rect(7, 34, 13, 30),
    pygame.Rect(38, 1, 19, 30),
    root_sprite]
)

def main():
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                s.set_action(core.Action(move=Chase(speed=speed, target=(10, 10)), animation=createGo()))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                s.set_action(core.Action(move=Chase(speed=speed, target=(570, 10)), animation=createBack()))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                s.set_action(core.Action(move=Chase(speed=speed, target=(10, 570))))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                s.set_action(core.Action(move=Chase(speed=speed, target=(570, 570))))
                s.set_action(core.Action(move=Chase(speed=speed, target=pygame.mouse.get_pos())))
        s.update()
        screen.blit(background, (0,0))
        screen.blit(s.image, s.rect, s.pic)
        pygame.display.update()
main()

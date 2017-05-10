import core
from core import Chase
from helper import *
import pygame

screen = init((600, 600), "chimps jumping")

chimp_image, chimp_rect = load_image("chimp.bmp")
c1 = core.GameObject(chimp_image, chimp_rect)
c2 = core.GameObject(chimp_image, chimp_rect)

trevor_image, trevor_rect = load_image("simon.png")
t1 = core.GameObject(trevor_image, pygame.Rect(0, 0, 90, 90))

speed = 50

#upLeft = core.Action(move=FirstDegree(speed*-1,2, 0.3, lenght=20))
#downRight = core.Action(move=FirstDegree(speed, 2, 0.3, lenght=20))
#downLeft = core.Action(move=FirstDegree(speed*-1, 2, 0.3, lenght=20))

clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

def main():
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                c1.set_action(core.Action(move=Chase(speed=speed, target=(10, 10))))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                c1.set_action(core.Action(move=Chase(speed=speed, target=(570, 10))))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                c1.set_action(core.Action(move=Chase(speed=speed, target=(10, 570))))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print(pygame.mouse.get_pos())
                c1.set_action(core.Action(move=Chase(speed=speed, target=(570, 570))))
                c1.set_action(core.Action(move=Chase(speed=speed, target=pygame.mouse.get_pos())))

        c1.update()
        t1.update()
        print(t1.size)
        screen.blit(background, (0,0))
        screen.blit(c1.image, c1.rect)
        screen.blit(t1.image, t1.rect, pygame.Rect(10, 10, 30, 70) )
        pygame.display.update()
main()

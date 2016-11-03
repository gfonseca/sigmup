import core
from core import Chase
from helper import *
import pygame

screen = init((600, 600), "chimps jumping")

chimp_image, chimp_rect = load_image("chimp.bmp")
chimp_rect = pygame.Rect((0, 0), (1, 1))
c1 = core.GameObject(chimp_image, chimp_rect)

speed = 20


#upLeft = core.Action(move=FirstDegree(speed*-1,2, 0.3, lenght=20))
#downRight = core.Action(move=FirstDegree(speed, 2, 0.3, lenght=20))
#downLeft = core.Action(move=FirstDegree(speed*-1, 2, 0.3, lenght=20))

clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

def main():
    while 1:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP7:
                c1.set_action(core.Action(move=Chase(speed=speed, target=(10, 10))))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP9:
                c1.set_action(core.Action(move=Chase(speed=speed, target=(570, 10))))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
                c1.set_action(core.Action(move=Chase(speed=speed, target=(10, 570))))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP3:
                c1.set_action(core.Action(move=Chase(speed=speed, target=(570, 570))))

        c1.update()
        screen.blit(background, (0,0))
        screen.blit(c1.image, c1.rect)
        pygame.display.update()
        
main()

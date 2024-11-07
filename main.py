import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400,720))
clock = pygame.time.Clock()
game = Game("imgs\\bird.png","imgs\pipe.png","imgs\\background.png","imgs\ground.png")
game.resize_images()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    game.show_background(screen)
    game.bear(screen)

    pygame.display.update()
    clock.tick(120)
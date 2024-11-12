import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400,720))
clock = pygame.time.Clock()
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,2500)
game = Game("imgs\\bird.png","imgs\pipe.png","imgs\\background.png","imgs\ground.png")
game.resize_images()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                game.flap()
            if event.key == pygame.K_SPACE and not game.active:
                game.restart()

        if event.type == SPAWNPIPE:
            game.add_pipe()

    game.show_background(screen)
    game.show_ground(screen)

    if game.active:
        game.move_ground()
        game.show_bird(screen)
        game.update_bird()
        game.move_pipes()
        game.show_pipes(screen)
        game.check_collision()
        game.update_score()
        game.show_score("playing",screen,(255,255,255))
    else:
        game.game_over(screen, (255,255,255))

    pygame.display.update()
    clock.tick(120)
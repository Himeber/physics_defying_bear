import pygame
import random

class Game:
    def __init__(self,bird_img,pipe_img,background_img,ground_img):
        self.bird = pygame.image.load(bird_img).convert_alpha()
        self.bird_rect = self.bird.get_rect(center = (70,180))
        self.pipe = pygame.image.load(pipe_img).convert_alpha()
        self.background = pygame.image.load(background_img).convert_alpha()
        self.ground = pygame.image.load(ground_img).convert_alpha()
        self.ber = pygame.image.load("imgs\\bear.png")

    def resize_images(self):
        self.bird = pygame.transform.scale(self.bird,(51,34))
        self.pipe = pygame.transform.scale(self.pipe,(80,438))
        self.background = pygame.transform.scale(self.background,(400,700))
        self.ground = pygame.transform.scale(self.ground,(470,160))
        self.ber = pygame.transform.scale(self.ber,(120,100))
    
    def show_background(self,screen):
        screen.blit(self.background,(0,0))
    
    def bear(self,screen):
        screen.blit(self.ber,(200,100))
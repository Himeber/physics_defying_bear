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
        self.ground_position = 0
        self.active = True
        self.gravity = 0.05
        self.bird_movement = 0
        self.rotated_bird = pygame.Surface((0,0))
        self.pipes = []
        self.pipe_height = [300, 425, 562]
        self.score = 0 
        self.font = pygame.font.SysFont(None,48)
        self.high_score = 0

    def resize_images(self):
        self.bird = pygame.transform.scale(self.bird,(51,34))
        self.pipe = pygame.transform.scale(self.pipe,(80,438))
        self.background = pygame.transform.scale(self.background,(400,700))
        self.ground = pygame.transform.scale(self.ground,(470,160))
        self.ber = pygame.transform.scale(self.ber,(120,100))
    
    def show_background(self,screen):
        screen.blit(self.background,(0,0))
    
    def show_ground(self,screen):
        screen.blit(self.ground,(self.ground_position,650))
        
    def move_ground(self):
        self.ground_position -= 1
        self.ground_position %= 45
        self.ground_position -= 45

    def show_bird(self,screen):
        screen.blit(self.rotated_bird,self.bird_rect)

    def rotate_bird(self):
        #scale and zoom
        new_bird = pygame.transform.rotozoom(self.bird, -self.bird_movement *3, 1)
        return new_bird

    def update_bird(self):
        self.bird_movement += self.gravity
        self.rotated_bird = self.rotate_bird()
        self.bird_rect.centery += self.bird_movement 

    def flap(self):
        self.bird_movement = 0
        self.bird_movement -= 2.5

    def add_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe.get_rect(midtop = (600,random_pipe_pos))
        top_pipe = self.pipe.get_rect(midbottom = (600,random_pipe_pos-211))
        self.pipes.append(bottom_pipe)
        self.pipes.append(top_pipe)

    def move_pipes(self):
        for pipe in self.pipes:
            pipe.centerx -= 1
            if pipe.centerx <= -40:
                self.pipes.remove(pipe)

    def show_pipes(self,screen):
        for pipe in self.pipes:
            if pipe.bottom >= 700:
                screen.blit(self.pipe,pipe)
            else:
                screen.blit(pygame.transform.flip(self.pipe,False,True),pipe)
    
    def check_collision(self):
        for pipe in self.pipes:
            if self.bird_rect.colliderect(pipe):
                self.active = False
        if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 650:
            self.active = False

    def bear(self,screen):
        screen.blit(self.ber,(200,100))

    def update_score(self):
        self.score += 0.01
    
    def show_score(self,game_state,screen,color):
        if game_state == "playing":
            score_surface = self.font.render(str(int(self.score)), True, color)
            score_rect = score_surface.get_rect(center = (202,75))
            screen.blit(score_surface,score_rect)
        
        elif game_state == "game_over":
            restart_text1 = self.font.render("Press Spacebar",True,color)
            restart_rect1 = restart_text1.get_rect(center = (200,280))
            screen.blit(restart_text1,restart_rect1)
            
            restart_text2 = self.font.render("to play again",True,color)
            restart_rect2 = restart_text2.get_rect(center = (200,340))
            screen.blit(restart_text2,restart_rect2)

            high_score = self.font.render(f"High Score: {str(self.high_score)}",True,color)
            high_rect = high_score.get_rect(center = (200,610))
            screen.blit(high_score,high_rect)
    
    def game_over(self,screen,color):
        self.update_high_score()
        self.show_score("game_over",screen,color)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = int(self.score)

    def restart(self):
        self.pipes = []
        self.active = True
        self.bird_rect.center = (70,180)
        self.bird_movement = 0
        self.score = 0
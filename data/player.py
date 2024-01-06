import pygame as pg    
from settings import *

class Player:
    def __init__(self, game):
        self.game = game   
        self.x, self.y = PLAYER_POS
        self.life = 100
        self.player_atack_esquerda = pg.image.load('textures/player/player_img_esquerda_ataque.png')
        self.player_atack_direita = pg.image.load('textures/player/player_img_direita_ataque.png')
        
    def movement(self):
        dx, dy = 0, 0 
        speed = PLAYER_SPEED * self.game.delta_time
    
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            dy -= speed

        if keys[pg.K_s]:
            dy += speed

        if keys[pg.K_a]:
            dx -= speed
            self.game.player_img = self.game.player_esquerda

        if keys[pg.K_d]:
            dx += speed
            self.game.player_img = self.game.player_direita
    
        self.check_wall_colision(dx, dy)
     
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_colision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx     
        
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy
    
    def atack(self):
        mouse = pg.mouse.get_pressed()
        self.distance = ((self.game.bandit.x * 64 - self.x * 64)**2 + (self.game.bandit.y * 64 - self.y * 64)**2)**(0.5)
        
        if mouse[0]:
            self.game.player_img = self.player_atack_esquerda
            if self.distance <= PLAYER_ATACK_DIS:
                self.game.bandit.life -= PLAYER_ATACK
        
        if mouse[2]:
            self.game.player_img = self.player_atack_direita
            if self.distance <= PLAYER_ATACK_DIS:
                self.game.bandit.life -= PLAYER_ATACK
        
    def draw(self):
        self.player_rect = self.game.tela.blit(self.game.player_img, (self.x * 64 - 32, self.y * 64 - 32))
    
    def die(self):
        if self.life <= 0:
            self.game.game_over = True
    
    def update(self):
        self.movement()
        self.atack()
        self.die()
     
    @property
    def pos(self):
        return self.x, self.y, self.life
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
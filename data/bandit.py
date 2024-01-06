import pygame as pg  
from settings import *

class Bandit:
    def __init__(self, game, bandit_pos, speed):
        self.game = game
        self.x, self.y = bandit_pos
        self.life = 64
        self.speed = speed
        self.bandit_esquerda_ataque = pg.image.load('textures/bandit/bandit_esqueda_ataque.png')
        self.bandit_direta_ataque = pg.image.load('textures/bandit/bandit_direita_ataque.png')
        self.bandit_morto = pg.image.load('textures/bandit/bandit_morto.png')
        
    def draw(self):
        self.game.tela.blit(self.game.bandit_img, (self.x * 64 - 32, self.y * 64 - 32))
        pg.draw.rect(self.game.tela, (0, 0, 0), (self.x * 64 + 1 - 32, self.y * 64 + 1 - (11 + 32), 64 + 2, 10 + 2))
        pg.draw.rect(self.game.tela, (255, 0, 0), (self.x * 64 - 32, self.y * 64 - (11 + 32), self.life, 10))
    
    def move_to_player(self):
        dx, dy = 0, 0
        speed = self.speed * self.game.delta_time
        
        if self.game.player.x < self.x:
            dx -= speed
            self.game.bandit_img = self.game.bandit_esquerda
        if self.game.player.x > self.x:
            dx += speed
            self.game.bandit_img = self.game.bandit_direita
                
        if self.game.player.y < self.y:
            dy -= speed  
        if self.game.player.y > self.y:
            dy += speed 

        self.detect_colision_to_atack()
        self.check_wall_colison(dx, dy)
    
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map  
    
    def check_wall_colison(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx      
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy
    
    def detect_colision_to_atack(self):
        self.distance = ((self.game.player.x * 64 - self.x * 64)**2 + (self.game.player.y * 64 - self.y * 64)**2)**(0.5)

        if self.distance <= BANDIT_ATACK_DIS:
            self.atack()
    
    def atack(self):
        if self.game.bandit_img == self.game.bandit_esquerda:
            self.game.bandit_img = self.bandit_esquerda_ataque
        if self.game.bandit_img == self.game.bandit_direita:
            self.game.bandit_img = self.bandit_direta_ataque
        self.game.player.life -= BANDIT_ATACK
    
    def die(self):
        if self.life <= 0:
            self.game.bandit_img = self.bandit_morto
        else:
            self.move_to_player()
        
            
    def update(self):
        self.die()
            
    @property
    def pos(self):
        return self.x, self.y, self.life
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
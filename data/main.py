import pygame as pg  
import sys
from settings import *
from map import *
from player import *
from bandit import *
from gui import *

class Game:
    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.player_esquerda = pg.image.load('textures/player/player_img_esquerda.png')
        self.player_direita = pg.image.load('textures/player/player_img_direita.png')
        self.player_img = self.player_direita
        self.bandit_esquerda = pg.image.load('textures/bandit/bandit_esquerda.png')
        self.bandit_direita = pg.image.load('textures/bandit/bandit_direita.png')
        self.bandit_img = self.bandit_direita
        self.pause = False
        self.game_over = False   
        self.new_game()
    
    def restart(self):
        game = Game()
        game.run()
    
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.bandit = Bandit(self, BANDIT_POS, BANDIT_SPEED)
        self.gui = GUI(self)
    
    def update(self):
        self.player.update()
        self.bandit.update()
        self.bandit.update()
        
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption('Be an Hero')
        
        
    def draw(self):
        self.tela.fill((0, 0, 0))
        
        self.map.draw()
        self.player.draw()
        self.bandit.draw()
        self.gui.draw()
        
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def run(self):
        while True:
            self.check_events()
            if self.pause == False and self.game_over == False:
                self.update()
                self.draw()
            elif self.game_over == True:
                self.gui.gameover()
                
            elif self.pause == True:
                self.tela.fill((0, 0, 0))
                self.gui.settings()
             

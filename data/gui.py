import pygame as pg   
import sys
from settings import *

class Settings:
    def __init__(self, reset, pause):
        pg.init()
        self.tela = pg.display.set_mode((1024, 640))
        self.clock = pg.time.Clock()
        self.pause = pause  
        self.reset = reset

    def title(self):
        title_img = pg.image.load('textures/gui/settings_title.png').convert()
        self.tela.blit(title_img, (312, 150))
    
    def buttons(self):
        button_img = pg.image.load('textures/gui/settings_back.png').convert()
        button = self.tela.blit(button_img, (312, 400))
        
        mouse, mouse_pos = pg.mouse.get_pressed(), pg.mouse.get_pos()
        
        if button.collidepoint(mouse_pos):
            if mouse[0]:
                self.pause = False
                self.reset()
        
    def update(self):
        pg.display.flip()
        self.clock.tick(60)
        pg.display.set_caption('Settings')
        
    def draw(self):
        self.tela.fill((0, 0, 0))
        self.title()
        self.buttons()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


class GameOver:
    def __init__(self, restart, game_over):
        pg.init()
        self.tela = pg.display.set_mode((1024, 640))
        self.clock = pg.time.Clock()
        self.game_over = game_over
        self.restart = restart
        
    def update(self):
        pg.display.flip()
        self.clock.tick(60)
        pg.display.set_caption('Game Over')
     
    def title(self):
        title_img = pg.image.load('textures/gui/game_over_title.png').convert()
        self.tela.blit(title_img, (312, 150))
    
    def buttons(self):
        button2_img = pg.image.load('textures/gui/game_over_restart.png').convert()
        mouse, mouse_pos = pg.mouse.get_pressed(), pg.mouse.get_pos()
        
                
        button2 = self.tela.blit(button2_img, (312, 500))
        if button2.collidepoint(mouse_pos):
            if mouse[0]:
                self.game_over = False  
                self.restart()
        
    def draw(self):
        self.tela.fill((0, 0, 0))
        self.title()
        self.buttons()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


class GUI:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.Font(None, 50)
    
    def Life_player(self):
        pg.draw.rect(self.game.tela, (0, 0, 0), (0, 0, 100 + 4, 30 + 4))
        pg.draw.rect(self.game.tela, (0, 255, 0), (0, 0, self.game.player.life, 30))
       
    def others(self): 
        text2 = self.font.render(f'FPS: {self.game.clock.get_fps() :.0f}', (255, 255, 255), True)
        self.game.tela.blit(text2, (300, 0))
    
    def status(self):
        pass  
    
    def pause(self):
        mouse = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        
        button_img = pg.image.load('textures/gui/button_settings.png').convert()
        button = self.game.tela.blit(button_img, (1024-100, 0))
        
        
        if button.collidepoint(mouse_pos):
            if mouse[0]:
                self.game.pause = True

    def gameover(self):
        gamever = GameOver(self.game.restart, self.game.game_over)
        gamever.run()
    
    def settings(self):
        settings = Settings(self.game.restart, self.game.pause)
        settings.run()
    
    def draw(self):
        self.Life_player()
        self.others()
        self.status()
        self.pause()
    
    def update(self):
        pass
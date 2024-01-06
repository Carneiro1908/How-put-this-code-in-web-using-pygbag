import pygame as pg   
from settings import *

_ = False  

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, 1, _, _, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, _, 1, _, 1, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, _, 1, _, 1, _, _, _, 1, _, _, _, _, 1],
    [1, _, _, 1, 1, _, _, _, 1, 1, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.tile_ocupado = pg.image.load('textures/map/tile_ocupado.png').convert()
        self.get_map()
        
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                    
    def draw(self):
        [self.game.tela.blit(self.tile_ocupado, (pos[0] * 64, pos[1] * 64))
         for pos in self.world_map]
        
        
        
import pygame as pg   
import sys
from main import *
import asyncio

class Menu:
    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode((900, 600))
        self.clock = pg.time.Clock()

    async def title(self):
        title_img = pg.image.load('textures/menu/menu_title.png').convert() 
        self.tela.blit(title_img, (0, 0))
    
    async def buttons(self):
        button_img = pg.image.load('textures/menu/menu_button.png').convert()
        mouse, mouse_pos = pg.mouse.get_pressed(), pg.mouse.get_pos()
        
        button = self.tela.blit(button_img, (0, 300))
        
        if button.collidepoint(mouse_pos):
            if mouse[0]:
                game = Game()
                task1 = asyncio.create_task(game.run())
                await asyncio.gather(task1)
                
    async def update(self):
        pg.display.flip()
        self.clock.tick(60)
        await asyncio.sleep(0)
        pg.display.set_caption('Be an Hero 1.0 - by TomasLima')
        
    async def draw(self):
        self.tela.fill((0, 0, 0))
        await self.title()
        await self.buttons()
        
    async def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pass
                
    async def run(self):
        while True:
            await self.check_events()
            await self.update()
            await self.draw()

menu = Menu()
asyncio.run(menu.run())
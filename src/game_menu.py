import pyglet
import game_assets

def draw_menu():
    game_assets.background.blit(0, 0)
    game_assets.title.blit(640, 450)
    game_assets.batch.draw()

def draw_tutorial():
    game_assets.background.blit(0, 0)

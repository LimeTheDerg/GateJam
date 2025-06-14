import game_assets
import gate
import prongs
import pyglet
import event_bus

def draw_menu():
    game_assets.background.blit(0, 0)
    game_assets.title.blit(640, 450)
    game_assets.menu_batch.draw()

def draw_tutorial():
    game_assets.tutorial.blit(0, 0)
    game_assets.tutorial_batch.draw()

def draw_game():
    game_assets.background.blit(0, 0)
    gate.gate_batch.draw()
    prongs.prong_middle.draw()
    pyglet.text.Label(
        text=str(event_bus.frame//18),
        x=0,
        y=0,
        font_size=30,
        color=(0, 0, 0)
    ).draw()
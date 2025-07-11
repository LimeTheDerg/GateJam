import game_assets
import gate
import prongs
import pyglet
import event_bus
import lime

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
    prongs.prong_middle.y = 135 + 200*(event_bus.frame/2300)
    prongs.prong_middle.draw()
    pyglet.text.Label(
        text="Score: " + str(event_bus.score),
        x=0,
        y=0,
        font_size=30,
        color=(255, 255, 255)
    ).draw()

def draw_end():
    game_assets.background.blit(0, 0)
    pyglet.text.Label(
        text="Your Final Score was: " + str(event_bus.score),
        x=320,
        y=360,
        font_size=30,
        color=(255, 255, 255),
        font_name='monospace',
        anchor_x='center',
        anchor_y='center'
    ).draw()
    lime.lime.scale_y = 1
    lime.lime.scale_x = 1
    lime.lime.image = game_assets.lime_good_img
    lime.lime_batch.draw()
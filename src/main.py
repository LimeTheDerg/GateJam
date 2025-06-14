import pyglet
import event_bus
from src.game_assets import music

# Initializes the window
game = pyglet.window.Window(width=1280, height=720)
game.set_visible(True)

from game_menu import *

@game.event
def on_draw():
    game.clear()
    if event_bus.page is event_bus.Pages.MENU:
        draw_menu()
    elif event_bus.page is event_bus.Pages.TUTORIAL:
        draw_tutorial()
    elif event_bus.page is event_bus.Pages.GAME:
        draw_game()

import game_assets
@game.event
def on_mouse_press(x, y, button, modifiers):
    if game_assets.is_clicked(x, y):
        game.clear()
        game.dispatch_event('on_draw')

# Game logic goes in this function so frame rate can stay consistent
def update(dt):
    if event_bus.page == event_bus.Pages.GAME:
        event_bus.frame += 1
    if event_bus.frame == 72:
        music.play()

pyglet.clock.schedule_interval(update, 1 / 30)  # Run at 30 FPS

pyglet.app.run()

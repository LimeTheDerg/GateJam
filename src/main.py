import pyglet
import event_bus

game = pyglet.window.Window(width=1280, height=720)
game.set_visible(True)

def update(dt):
    pass

from game_menu import *
pyglet.clock.schedule_interval(update, 1 / 60.0)  # Run at 60 FPS

@game.event
def on_draw():
    game.clear()
    if event_bus.page is event_bus.Pages.MENU:
        draw_menu()
    elif event_bus.page is event_bus.Pages.TUTORIAL:
        draw_tutorial()

import game_assets
@game.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y)
    if game_assets.is_clicked(x, y):
        game.clear()
        game.dispatch_event('on_draw')

pyglet.app.run()

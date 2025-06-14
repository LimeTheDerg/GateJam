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
    elif event_bus.page is event_bus.Pages.END:
        draw_end()

import game_assets
@game.event
def on_mouse_press(x, y, button, modifiers):
    if event_bus.page is not event_bus.Pages.END:
        gate.check_false_press()
    game_assets.is_clicked(x, y)
    if button == pyglet.window.mouse.LEFT:
        event_bus.LMBdown = True
    elif button == pyglet.window.mouse.RIGHT:
        event_bus.RMBdown = True

@game.event
def on_mouse_release(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        event_bus.LMBdown = False
    elif button == pyglet.window.mouse.RIGHT:
        event_bus.RMBdown = False

import gate
from BooPeeBoSong import notes
# Game logic goes in this function so frame rate can stay consistent
def update(dt):
    gate.check_collision()
    if event_bus.page == event_bus.Pages.GAME:
        event_bus.frame += 1
        if event_bus.frame/18+4 in notes:
            gate.spawn_gate()
        gate.move_gate(dt)
        if event_bus.frame == 2550:
            event_bus.page = event_bus.Pages.END
    if event_bus.frame == 90 and event_bus.playing is False:
        music.play()
        event_bus.frame = 2000 # was 18
        event_bus.playing = True

pyglet.clock.schedule_interval(update, 1 / 30)  # Run at 30 FPS
pyglet.app.run()

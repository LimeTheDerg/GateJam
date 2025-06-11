import pyglet

page = "menu"

game = pyglet.window.Window(width=1280, height=720)
game.set_visible(True)

from game_menu import draw_menu

@game.event
def on_draw():
    game.clear()
    if page == "menu":
        draw_menu()


pyglet.app.run()

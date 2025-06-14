
import pyglet
import event_bus
import sys, os

def resource_path(path):
    try:
        base = sys._MEIPASS
    except AttributeError:
        base = os.path.abspath(".")
    return os.path.join(base, path)

menu_batch = pyglet.graphics.Batch()
tutorial_batch = pyglet.graphics.Batch()

# The various assets used in the game

# The actual song
music = pyglet.media.load(resource_path('assets/song.mp3'))

# Background
background = pyglet.image.load(resource_path('assets/GateJamBG.png'))

# Title
title = pyglet.image.load(resource_path('assets/GateJamLogo.png'))
title.anchor_x = title.width // 2
title.anchor_y = title.height // 2

# Start Button
startButtonImg = pyglet.image.load(resource_path('assets/StartButton.png'))
startButtonImg.anchor_x = startButtonImg.width // 2
startButtonImg.anchor_y = startButtonImg.height // 2
startButton = pyglet.sprite.Sprite(
    x=640,
    y=200,
    batch=menu_batch,
    img=startButtonImg
)

# Tutorial Screen
tutorial = pyglet.image.load(resource_path('assets/GateJamTutorial.png'))

# Finish Tutorial Button
finishTutButtonImg = pyglet.image.load(resource_path('assets/FinishTutorial.png'))
finishTutButton = pyglet.sprite.Sprite(
    x=0,
    y=0,
    batch=tutorial_batch,
    img=finishTutButtonImg
)

# Gate images
or_gate = pyglet.image.load(resource_path('assets/OR.png'))
or_gate.anchor_x = or_gate.width // 2
or_gate.anchor_y = or_gate.height // 2

and_gate = pyglet.image.load(resource_path('assets/AND.png'))
and_gate.anchor_x = and_gate.width // 2
and_gate.anchor_y = and_gate.height // 2

not_gate = pyglet.image.load(resource_path('assets/NOT.png'))
not_gate.anchor_x = not_gate.width // 2
not_gate.anchor_y = not_gate.height // 2

# Lime the dragon
lime_good_img = pyglet.image.load(resource_path('assets/LimeGood.png'))
lime_bad_img = pyglet.image.load(resource_path('assets/LimeBad.png'))



# Functions to determine if something is being clicked
def is_clicked(x, y):
    # Check if it's the start button at the very beginning
    if 640-startButton.width//2 < x < 640+startButton.width//2 and 200-startButton.height//2 < y < 200+startButton.height//2 and event_bus.page == event_bus.Pages.MENU:
        event_bus.page = event_bus.Pages.TUTORIAL
    # Or the finish tutorial button
    if 0 < x < finishTutButton.width and 0 < y < finishTutButton.height and event_bus.page == event_bus.Pages.TUTORIAL:
        event_bus.page = event_bus.Pages.GAME
        event_bus.score = 0

import pyglet
import event_bus
batch = pyglet.graphics.Batch()

# The various assets used in the game
# Background
background = pyglet.image.load('../assets/GateJamBG.png')

# Title
title = pyglet.image.load('../assets/GateJamLogo.png',)
title.anchor_x = title.width // 2
title.anchor_y = title.height // 2

# Start Button
startButtonImg = pyglet.image.load('../assets/StartButton.png')
startButtonImg.anchor_x = startButtonImg.width // 2
startButtonImg.anchor_y = startButtonImg.height // 2
startButton = pyglet.sprite.Sprite(
    x=640,
    y=200,
    batch=batch,
    img=startButtonImg
)



# Functions to determine if something is being clicked
def is_clicked(x, y):
    if 640-startButton.width//2 < x < 640+startButton.width//2 and 200-startButton.height//2 < y < 200+startButton.height//2:
        event_bus.page = event_bus.Pages.TUTORIAL
        return True
    return False

import event_bus
import game_assets
import pyglet


lime_bad_frames = 0
up_vibe = False
down_vibe = True

lime_batch = pyglet.graphics.Batch()
lime = pyglet.sprite.Sprite(
    x=-100,
    y=0,
    batch=lime_batch,
    img=game_assets.lime_good_img
)


def lime_bounce():
    global up_vibe, down_vibe,lime_bad_frames
    if lime_bad_frames > 0:
        lime_bad_frames -= 1
    if lime_bad_frames <= 0:
        lime.image=game_assets.lime_good_img
    if lime_bad_frames > 0:
        lime.image=game_assets.lime_bad_img
    if event_bus.frame % 9 == 0 and up_vibe:
        down_vibe = True
        up_vibe = False
    if event_bus.frame % 18 == 0 and down_vibe:
        up_vibe = True
        down_vibe = False
    if up_vibe:
        lime.scale_y += 0.0065
        lime.scale_x -= 0.0025
    if down_vibe:
        lime.scale_y -= 0.0065
        lime.scale_x += 0.0025
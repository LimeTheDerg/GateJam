import random

import pyglet
import game_assets

gate_batch = pyglet.graphics.Batch()

gates_in_play = []

def spawn_gate():
    gate = random.randint(1,5)
    if gate == 1 or gate == 2:
        or_gate = pyglet.sprite.Sprite(
            x=320,
            y=850,
            img=game_assets.or_gate,
            batch=gate_batch
        )
        gates_in_play.append(or_gate)
    elif gate == 3 or gate == 4:
        and_gate = pyglet.sprite.Sprite(
            x=320,
            y=850,
            img=game_assets.and_gate,
            batch=gate_batch
        )
        gates_in_play.append(and_gate)
    elif gate == 5:
        not_gate = pyglet.sprite.Sprite(
            x=320,
            y=850,
            img=game_assets.not_gate,
            batch=gate_batch
        )
        gates_in_play.append(not_gate)

def move_gate(dt):
    for gate in gates_in_play:
        gate.y -= 300 * dt
        if gate.y < -30:
            gates_in_play.remove(gate)
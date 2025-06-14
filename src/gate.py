import random
from enum import Enum
import pyglet
import game_assets
import event_bus

gate_batch = pyglet.graphics.Batch()

gates_in_play = []

class Gates(Enum):
    OR = 1
    AND = 2
    NOT = 3

class Gate:
    type_of_gate = None
    sprite = None

    def __init__(self, type_of_gate, sprite):
        self.type_of_gate = type_of_gate
        self.sprite = sprite

def spawn_gate():
    gate = random.randint(1,5)
    if gate == 1 or gate == 2:
        or_gate = pyglet.sprite.Sprite(
            x=320,
            y=850,
            img=game_assets.or_gate,
            batch=gate_batch
        )
        new_gate = Gate(Gates.OR, or_gate)
        gates_in_play.append(new_gate)
    elif gate == 3 or gate == 4:
        and_gate = pyglet.sprite.Sprite(
            x=320,
            y=850,
            img=game_assets.and_gate,
            batch=gate_batch
        )
        new_gate = Gate(Gates.AND, and_gate)
        gates_in_play.append(new_gate)
    elif gate == 5:
        not_gate = pyglet.sprite.Sprite(
            x=320,
            y=850,
            img=game_assets.not_gate,
            batch=gate_batch,
        )
        new_gate = Gate(Gates.NOT, not_gate)
        gates_in_play.append(new_gate)

def move_gate(dt):
    for gate in gates_in_play:
        gate.sprite.y -= 300 * dt + (event_bus.frame//1000)
        if gate.sprite.y < -30:
            gates_in_play.remove(gate)

def check_collision():
    for gate in gates_in_play:
        if gate.sprite.y+gate.sprite.height//2 > 135 > gate.sprite.y-gate.sprite.height//2:
            if gate.type_of_gate is Gates.OR and (event_bus.LMBdown or event_bus.RMBdown) is True:
                event_bus.score += 100
                gates_in_play.remove(gate)
            elif gate.type_of_gate is Gates.AND and (event_bus.LMBdown and event_bus.RMBdown) is True:
                event_bus.score += 100
                gates_in_play.remove(gate)
            elif gate.type_of_gate is Gates.NOT and (event_bus.LMBdown or event_bus.RMBdown) is True:
                event_bus.score -= 200
                gates_in_play.remove(gate)
        if 0 > gate.sprite.y and gate.type_of_gate is Gates.NOT:
            event_bus.score += 100
            gates_in_play.remove(gate)
        if 0 > gate.sprite.y and gate.type_of_gate is not Gates.NOT:
            event_bus.score -= 200
            gates_in_play.remove(gate)

def check_false_press():
    flag = False
    for gate in gates_in_play:
        if gate.sprite.y+gate.sprite.height//2 > 135 > gate.sprite.y-gate.sprite.height//2:
            flag = True

    if flag is False:
        event_bus.score -= 200
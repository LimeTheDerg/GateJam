import enum

class Pages(enum.Enum):
    MENU = 1
    TUTORIAL = 2
    GAME = 3

page = Pages.MENU

frame = 0

score = 0

playing = False

LMBdown = False
RMBdown = False

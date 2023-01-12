from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.constants import SINGLE_LINE
from .constants import *
from .utils import show_effects, gridpos2dpos
from cardio import GridPos


def draw_slot_in_grid(screen, pos: GridPos):
    dpos = gridpos2dpos(pos)
    show_effects(
        screen,
        Print(
            screen=screen,
            renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE),
            x=dpos.x,
            y=dpos.y,
            colour=Screen.COLOUR_BLACK,
            attr=Screen.A_BOLD,
        ),
    )
    # (BLACK + BOLD produces dark gray,
    # cf https://github.com/peterbrittain/asciimatics/issues/363)


def draw_grid_decks_separator(screen, width: int) -> None:
    dpos = gridpos2dpos(GridPos(4, 0))
    show_effects(
        screen,
        Print(
            screen,
            StaticRenderer(["—" * ((BOX_WIDTH + BOX_PADDING_LEFT) * width + 4)]),
            x=dpos.x - 2,
            y=dpos.y - 3,
            colour=Screen.COLOUR_BLACK,
            attr=Screen.A_BOLD,
        ),
    )



from asciimatics.screen import Screen
from asciimatics.renderers import FigletText
from cardio import GridPos, session
from cardio.agent_damage_state import AgentDamageState
from .utils import dPos, render_value, show, show_text
from .constants import *


class StateWidget:
    NAME_FONT = "rectangles"
    # Options: rectangles, small, chunky, ... (http://www.figlet.org/examples.html)

    def __init__(
        self, screen: Screen, grid_width: int, damagestate: AgentDamageState
    ) -> None:
        self.screen = screen
        self.damagestate = damagestate
        x = dPos.from_gridpos(GridPos(0, grid_width)).x
        x += AGENT_X_OFFSET
        self.computer_pos = dPos(x, dPos.from_gridpos(GridPos(0, 0)).y)
        self.human_pos = dPos(x, dPos.from_gridpos(GridPos(2, 0)).y)

    def _show_health_bars(self, pos: dPos, diff: int, max_diff: int) -> None:
        bars = render_value(min(max_diff - diff, max_diff), "█ ", 100) + "\n"
        bars *= 2
        show_text(self.screen, bars, pos, color=Color.CYAN)

    def show_computerplayer_state(self) -> None:
        show(
            self.screen,
            FigletText("Yshl", self.NAME_FONT),
            self.computer_pos,
            color=Color.GRAY,
        )
        self._show_health_bars(
            dPos(self.computer_pos.x, self.computer_pos.y + 8),
            -self.damagestate.diff,
            self.damagestate.max_diff,
        )

    def show_humanplayer_state(self) -> None:
        self._show_health_bars(
            self.human_pos, self.damagestate.diff, self.damagestate.max_diff
        )
        state_str = f"""\
{FigletText("Schnuzgi", self.NAME_FONT)}
{render_value(session.humanplayer.lives, '💓', surplus_color=Screen.COLOUR_RED)}
{render_value(session.humanplayer.gems, '💎', surplus_color=Screen.COLOUR_BLUE)}
{render_value(session.humanplayer.spirits, '👻')}
"""
        show_text(
            self.screen,
            state_str,
            dPos(self.human_pos.x, self.human_pos.y + 2),
            color=Color.GRAY,
        )
        # TODO Support something like dPos(1,1)+(1,1)

    def show_all(self):
        self.show_computerplayer_state()
        self.show_humanplayer_state()


# Alternative scale:
#         🔳
#         🔳
#         🔳
#         🔳
#         🔳
# ▶️ or 👉 🟥
#         🔳
#         🔳
#         🔳
#         🔳
#         🔳

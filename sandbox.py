# %%
import logging
from cardio import Card, session
from cardio.tui import tui
from cardio.agent_strategies import Turn0OnlyStrategy, GridPos, SimpleHumanStrategy

logging.basicConfig(level=logging.DEBUG)

cs = Turn0OnlyStrategy(
    [
        # type:ignore
        (GridPos(0, 1), Card(name="Steed", initial_power=2, initial_health=10)),
        (GridPos(1, 0), Card(name="Dog", initial_power=2, initial_health=5)),
    ]
)

session.setup()
hs = SimpleHumanStrategy(session.grid)
# handlers.handle_fight(computerstrategy=cs, humanstrategy=hs)
# fight = Fight(grid=session.grid, computeragent=session.computeragent, humanagent=session.humanagent, computerstrategy=cs, humanstrategy=None)
tv = tui.TUIViewAndController(debug=True, grid=session.grid)
session.view = tv
tv.handle_fight(computerstrategy=cs)
tv.close()

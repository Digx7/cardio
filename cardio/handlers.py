from . import session
from . import commands
from . import events

# ---------- events ----------


def gets_attacked(event: events.CardGetsAttacked) -> None:
    event.target.get_attacked(event.attacker)
    session.view.update()


HANDLERS = {
    events.CardGetsAttacked: [gets_attacked],
}


# ---------- commands ----------


def handle_all_events() -> None:
    while session.events:
        e = session.events.pop(0)
        handlers = HANDLERS.get(type(e), [])
        for h in handlers:
            h(e)


def handle_turn(cmd: commands.HandleTurn) -> None:

    # for linei, opponenti in ((2, 1), (1, 2)):
    #     for sloti in range(self.grid.width):
    #         if self.grid[linei][sloti] is None:
    #             continue  # No card in this slot
    #         if self.grid[opponenti][sloti] is None:
    #             # FIXME Damage the player behind
    #             continue
    #         self.grid[linei][sloti].attack(self.grid[opponenti][sloti])

    # FIXME Need some activate method instead of attack.
    # FIXME Then need to add line 0 as well.
    # FIXME It becomes apparent here: Terms like opponent and player are overloaded.
    # FIXME A card that is dead should be removed.

    # Activate player cards
    session.grid.playerline.activate()
    handle_all_events()
    # Activate opponent cards
    session.grid.opponentline.activate()
    handle_all_events()
    # Activate from prepline
    session.grid.prepline.prepare()
    handle_all_events()

    # FIXME Check if game over

    session.view.update()  # FIXME Should be done automatically somewhere?


# def add_card(cmd: commands.AddCard) -> None:
# # def add_card(self, linei: int, sloti: int, card: Card) -> None:
#     self.grid[linei][sloti] = card
#     self.gridview.update()

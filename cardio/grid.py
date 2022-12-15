from typing import List, Optional, Tuple
import logging
from cardio.card import Card


class Line:
    """

    Slots are counted 0, 1, 2, ... from left border.
    """

    def __init__(self, width: int) -> None:
        self.slots: List[Optional[Card]] = [None] * width

    def __getitem__(self, sloti: int) -> Optional[Card]:
        return self.slots[sloti]

    def __setitem__(self, sloti, card: Card) -> None:
        self.slots[sloti] = card

    def __iter__(self) -> object:
        return self.slots.__iter__()

    def add_card(self, sloti: int, card: Card) -> None:
        self[sloti] = card

    def prepare(self) -> None:
        pass

    def activate(self) -> None:
        for card in self.slots:
            if card is None:
                continue
            card.activate()


class Grid:
    def __init__(self, width: int = 4) -> None:
        self.width = width
        self.prepline = Line(width)
        self.opponentline = Line(width)
        self.playerline = Line(width)
        self.lines = [self.prepline, self.opponentline, self.playerline]
        # QQ: Should there be some CardSlot or some BaseCard or NoCard class for the
        # empty spaces?

    def __getitem__(self, linei):
        return self.lines[linei]

    def __iter__(self) -> object:
        return self.lines.__iter__()

    def find_card_position(self, card: Card) -> Tuple[Optional[int], Optional[int]]:
        for rowi, row in enumerate(self.lines):
            for sloti in range(self.width):
                if row[sloti] is card:
                    return (rowi, sloti)
        return (None, None)

    def find_opponent(self, card: Card) -> Optional[Card]:
        rowi, sloti = self.find_card_position(card)
        if rowi == 1:
            return self.lines[2][sloti]
        elif rowi == 2:
            return self.lines[1][sloti]
        return None

    def remove_card(self, card: Card) -> None:
        rowi, sloti = self.find_card_position(card)
        assert self[rowi][sloti] is card
        self[rowi][sloti] = None
        logging.debug("Removed card from [%s, %s]", rowi, sloti)

import random
from typing import Protocol, Type
from cardio import Card, CardList, skills
from cardio.human_player import HumanPlayer
from .location import Location
from .baseview import BaseLocationView


class SkillLotteryView(BaseLocationView, Protocol):
    def __init__(self, cards: CardList, *args, **kwargs) -> None:
        ...

    def pick(self, activecards: CardList) -> Card:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...


class SkillLotteryLocation(Location):
    """Add a random skill to a card.

    If the card already has skills, there is a chance that a random existing skill is
    removed rather than a new one added.

    Notes:
    - There are currently no restrictions as to which skills can and cannot be combined
      with which other skills. (Should there be?)
    """

    marker = "SL⚀"
    description = "Add a random skill to a card. 🎲"

    def generate(self) -> None:
        super().generate()

    def handle(self, view_class: Type[SkillLotteryView], humanplayer: HumanPlayer) -> bool:
        view = view_class(humanplayer.deck.cards, description=self.description)
        possible_cards = [
            c for c in humanplayer.deck.cards if c.skills.count() < Card.MAX_SKILLS
        ]
        if not possible_cards:
            view.error("Sorry, you don't have any cards that can get more skills.")
            return True
        card = view.pick(possible_cards)
        if card.skills and random.random() < card.skills.count() / Card.MAX_SKILLS:
            skill = random.choice(card.skills.get_types())
            card.skills.remove(skill)
            view.show_upgrade(card)
            view.message(f"{card.name} lost the {skill.name} {skill.symbol} skill. 😢")
        else:
            skill = random.choice(
                list(set(skills.get_skilltypes()) - set(card.skills.get_types()))
            )
            card.skills.add(skill)
            view.show_upgrade(card)
            view.message(f"{card.name} gained the {skill.name} {skill.symbol} skill! 🥳")

        view.close()
        return True

import logging
from cardio import gg, HumanPlayer
from cardio.card_blueprints import create_cards_from_blueprints
from cardio.run import Run
from cardio.tui.tuimapview import TUIMapView

logging.basicConfig(level=logging.DEBUG)

### Start menu: Create new or load existing player | start new run

### If create new player:
humanplayer = HumanPlayer(name="Schnuzgi", lives=1, spirits=3)
HUMAN_START_CARDS = ["Church Mouse", "Weasel", "Lynx", "Porcupine"]
humanplayer.deck.cards = create_cards_from_blueprints(HUMAN_START_CARDS)
gg.humanplayer = humanplayer

### If load player:
# (Load and just use the main deck the player has.)

### Start new run:
run = Run()  # <- This generates a new seed
# (or load seed + current location + player state if existing game is being continued)


### While not game over:
mapview = TUIMapView(run)
game_on = True
while game_on:
    chosen_loc = mapview.get_next_location()
    mapview.move_to(chosen_loc)
    run.move_to(chosen_loc)
    # game_on = chosen_loc.handle() TODO

# Going through the map:
# - Show map and mark current location. (Which is always on the lowest line in the map.)
# - Disable non-accessible paths (e.g. in dark gray) OR: Make everything dark grey and
#   highlight: current location, next locations to be chosen from, currently highlighted
#   next location, all accessible locations.
# - Mark all possible targets for the next location and place the cursor in the leftmost
#   of those.
# - Allow user to choose and confirm next location.
# - Visit/handle selected location.
# - Increase current_rung
# - Start from top of loop.

### Game over:
###   ...

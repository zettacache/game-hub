from enum import Enum, auto
from random import choice
from ..input_utils import get_expected_input


class AttackChoice(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class GameOutcome(Enum):
    PLAYER_WON = auto()
    COMPUTER_WON = auto()
    TIE = auto()


ACCEPTED_INPUTS = ['r', 'p', 's']
INPUT_MAP = {
    "r": AttackChoice.ROCK,
    "p": AttackChoice.PAPER,
    "s": AttackChoice.SCISSORS,
}
class RockPaperScissors:
    def __init__(self):
        self._game_loop()

    @staticmethod
    def find_winner(player: AttackChoice, computer: AttackChoice) -> GameOutcome:
        if player == computer:
            return GameOutcome.TIE

        # If not a tie, find the winner
        return GameOutcome.PLAYER_WON if (
            (player == AttackChoice.ROCK and computer == AttackChoice.SCISSORS)
            or (player == AttackChoice.SCISSORS and computer == AttackChoice.PAPER)
            or (player == AttackChoice.PAPER and computer == AttackChoice.ROCK)
        ) else GameOutcome.COMPUTER_WON

    def _game_loop(self):
        while True:
            user_input = get_expected_input("[r]ock, [p]aper, [s]cissors >> ", ACCEPTED_INPUTS)
            user_input_enum = INPUT_MAP[user_input]
            computer_input = choice(ACCEPTED_INPUTS)
            computer_input_enum = INPUT_MAP[computer_input]

            print(f"Computer chose {computer_input}")
            if (outcome := RockPaperScissors.find_winner(user_input_enum, computer_input_enum)) == GameOutcome.TIE:
                print("It's a tie!")
            else:
                print(f"{"You" if outcome == GameOutcome.PLAYER_WON else "The computer"} won!")
                break

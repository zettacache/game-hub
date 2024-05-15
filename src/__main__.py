from .app import App
from .games.rock_paper_scissors import RockPaperScissors
from .games.battle_ship import BattleShip


def main():
    App(game_list=[
        {
            "name": "Rock Paper Scissors",
            "loader": RockPaperScissors
        },
        {
            "name": "Battle Ship",
            "loader": BattleShip
        }
    ])


if __name__ == "__main__":
    main()

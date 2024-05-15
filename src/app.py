from .input_utils import get_expected_input

class App:
    """Location of general application logic"""
    def __init__(self, game_list):
        self.game_list = game_list
        self.choose_game_menu()

    def choose_game_menu(self):
        """
        Prints out available games and forces the user to choose one
        """
        print("Choose your game\n====================")
        for index, game in enumerate(self.game_list):
            print(f"{index}) {game["name"]}")

        user_input = get_expected_input("> ", [*range(len(self.game_list))])
        self.game_list[int(user_input)]["loader"]()

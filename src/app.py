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

        user_input = App.get_expected_input("> ", [*range(len(self.game_list))])
        self.game_list[int(user_input)]["loader"]()

    @staticmethod
    def get_expected_input(prompt: str, options: list) -> str:
        """
        Reads input from user and matches it against a provided
        list of accepted inputs.

        Args:
            prompt (str): The prompt upon requesting user input
            options (list): The list of accepted inputs

        Returns:
            str: The accepted user input
        """
        # We create a list that ensures all values in `options` are a string
        # to prevent type confliction.
        normalized_list = [str(x) for x in options]
        
        user_input = input(prompt)

        if user_input in normalized_list:
            return user_input
        else:
            print(f"Invalid input (expected: {options})")
            return App.get_expected_input(prompt, options)

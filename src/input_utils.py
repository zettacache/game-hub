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
        return get_expected_input(prompt, options)

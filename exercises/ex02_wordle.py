"""Exercise 02 Wordle game"""

__author__: str = "730641475"


def contains_char(word: str, char: str) -> bool:
    """checks if given char is anywhere in word"""
    assert len(char) == 1, f"len('{char}') is not 1"

    i: int = 0
    while i < len(word):

        if word[i] == char:
            # if a letter in word == char, then we can stop looking as it is true
            return True

        # we dont need an else here cause the function returns if true
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """loops through chars of word to print corresponding Wordle emojis"""

    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    response: str = ""

    i: int = 0

    while i < len(secret):
        if guess[i] == secret[i]:
            # if the i-th letter of guess == i-th letter of secret, it's green box
            response += GREEN_BOX
        else:
            # if it isn't the right letter

            if contains_char(word=secret, char=guess[i]):
                # if the letter is in the word, it's yellow
                response += YELLOW_BOX

            else:
                # if it is never in the word, it's white
                response += WHITE_BOX
        i += 1
    return response


def input_guess(expected_length: int) -> str:
    """asks user for guess, then checks if it is correct length. Returns guess"""
    guess: str = input(f"Enter a {expected_length} character word")

    # if the guess is the wrong length, start looping till you it's the right length
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} characters! Try again:")

    # once you exit the while loop,
    # it means guess = expected_length, so we should return the valid guess
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    game_ended: bool = False
    game_won: bool = False  # start not having won until meet win condition

    turn: int = 1
    while not game_ended:
        print(f"=== Turn {turn}/6 ===")

        valid_guess: str = input_guess(
            len(secret)
        )  # input guess validates the guess before progresses
        print(emojified(valid_guess, secret))

        if turn == 6:  # game ended but not won
            game_ended = True

        if valid_guess == secret:  # game won (and tfore ended)
            game_ended = True
            game_won = True

        if not game_ended:
            # should only increment score if the game is still running
            # could start at turn 0, then always +=1, but this works
            turn += 1

    if game_won:  # after exiting the loop, say you won in num turns
        print(f"You won in {turn}/6 rounds!")

    else:  # if you didn't win but the game ended, you must have lost
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")

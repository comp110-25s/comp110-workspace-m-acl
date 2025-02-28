"""this is the guessing game script"""

MYSTERY_WORD: str = "jarnathan"


def guessing_game(guess: str, key_word: str = MYSTERY_WORD, idx: int = 0) -> bool:

    if len(guess) == len(key_word):
        print("correct length")

        for i in range(0, len(key_word) - 1):
            if guess[i + idx] == key_word[i + idx]:
                print("we good so far")

            else:
                print("wrong letter")
                return False

        print(f"gg you got it right, the word was {key_word}")
        return True

    else:
        print("words are diff lengths")
        return False


# guessing_game(input("yo this is your guess for the guessing game\n"))


def mystery_game(guess: str, secret: str = MYSTERY_WORD, idx=0) -> bool:
    if idx < len(secret):

        if guess[idx] != secret[idx]:
            print(f"{guess[idx]} isnt the words first letter")
            return False

        else:
            print(
                f"{guess[idx]} is at index {idx} for both words! Checking next letters."
            )
            return mystery_game(guess, secret, idx + 1)

    if guess[idx - 1] == secret[idx - 1]:
        print("gg you got it")

    else:
        print("too long")

    return False


mystery_game(guess=input("this is ur guess for the mystery game\n"))

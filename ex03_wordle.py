"""Exercise 3 Structured Wordle."""

__author__ = "730702719"

GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
WHITE_BOX: str = "\U00002B1C"


def contains_char(secret_word: str, letter_check: str) -> bool: 
    """Checks the secret word for any instances of the letter being checked."""
    assert len(letter_check) == 1  # makes sure letter is 1 character
    loop_index: int = 0
    while loop_index < len(secret_word):  # uses seperate look index to look through all secret word characters
        if secret_word[loop_index] == letter_check:
            return True  # if letter is found true
        else:
            loop_index += 1  # if not go to next letter
    return False  # letter never found then contains_char is false


def emojified(user_guess:str, secret_word: str) -> str:
    """Checks the player guess and converts it to wordle emoji code."""
    assert len(secret_word) == len(user_guess)  # Makes sure secret word is same length as guess
    loop_index: int = 0
    emoji_return: str = ""
    while loop_index < len(secret_word):
        if secret_word[loop_index] == user_guess[loop_index]:  # if in the same index add green square
            emoji_return = emoji_return + GREEN_BOX
            loop_index += 1
        elif contains_char(secret_word, user_guess[loop_index]):  # if in the word but not same index add yellow square
            emoji_return = emoji_return + YELLOW_BOX
        else:
            emoji_return = emoji_return + WHITE_BOX  # if not in the word add grey square
            loop_index += 1
    return (emoji_return)


def input_guess(length: int) -> str:
    """Checks if input guess is same length as secret."""
    player_guess = input(f"Enter a { length } character word: ")
    while len(player_guess) != length:
        player_guess = input(f"That wasn't { length } chars! Try again: ")
    return player_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number = 1  # define which turn the player is on
    secret_word = "codes"  # defines secret word
    while turn_number < 7:  # made it less than 7 so all turns can be played out
        print(f"=== Turn { turn_number }/6 ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in { turn_number }/6 turns")  # lets the user know they won in X turns
            turn_number = 10  # this is so it doesnt print sorry after the loop is over
        else:
            turn_number += 1
    if turn_number == 7:  # only occurs when loop ran out with no correct answers
        print("X/6 - Sorry, try again tomorrow!")
    else:
        print()  # nothing extra if user was correct

el;

if __name__ == "__main__":
    main()  # runs main loop
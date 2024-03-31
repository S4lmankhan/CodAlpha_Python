# PROGRAM FOR HANGMAN GUESS GAME 
import random


def choose_word():
    word_list = ["python", "hangman", "developer", "coding", "challenge"]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman_game():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Hello Dear User You Only Have 7 Chances To Guess The Correct Word!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                incorrect_guesses += 1
                print(f"Incorrect guess! {max_incorrect_guesses - incorrect_guesses} guesses left.")

        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You've guessed it (; ")
    else:
        print(f"Out of guesses! The word was: {word_to_guess}")


hangman_game()

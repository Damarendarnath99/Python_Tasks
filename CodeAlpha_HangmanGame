import random

WORDS = ["python", "hangman", "computer", "keyboard", "program"]
MAX_WRONG = 6


def show_state(word, guessed, wrong_count):
    """Print the current word progress and the number of wrong guesses left."""
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord: " + display.strip())
    print("Wrong guesses left:", MAX_WRONG - wrong_count)


def play():
    word = random.choice(WORDS)
    guessed = []          # all letters guessed so far
    wrong_count = 0

    print("=== HANGMAN ===")
    print("Guess the word one letter at a time. You can miss up to", MAX_WRONG, "times.")

    while wrong_count < MAX_WRONG:
        show_state(word, guessed, wrong_count)
        if guessed:
            print("Guessed so far:", ", ".join(sorted(guessed)))

        # Check for a win: every letter of the word has been guessed
        all_found = True
        for letter in word:
            if letter not in guessed:
                all_found = False
        if all_found:
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("Enter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print("You already guessed '" + guess + "'. Try another.")
        else:
            guessed.append(guess)
            if guess in word:
                print("Good guess! '" + guess + "' is in the word.")
            else:
                wrong_count += 1
                print("Sorry, '" + guess + "' is not in the word.")

    print("\nGame over! You ran out of guesses. The word was:", word)


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

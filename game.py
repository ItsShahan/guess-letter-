import random

def pick_random_word():
    words = ["apple", "banana", "cherry", "grape", "orange", "watermelon", "pineapple", "strawberry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman_game():
    word = pick_random_word()
    guessed_letters = []
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word!")
            break

        if len(guessed_letters) == max_attempts:
            print("Sorry, you're out of attempts. The word was:", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")

if __name__ == "__main__":
    hangman_game()

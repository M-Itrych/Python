import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

secret_word = random.choice(word_list)
blank_list = ["_"] * len(secret_word)
lives = 6
print(logo)

while True:
    user_guess = input("Guess a letter: ").lower()
    if user_guess in blank_list:
        print(f"You have already guessed {user_guess}!")
        print(" ".join(blank_list))
        print(stages[lives])
        pass
    if user_guess in secret_word:
        for i in range(len(secret_word)):
            if user_guess == secret_word[i]:
                blank_list[i] = user_guess
        print("You've guessed the right letter")
        print(" ".join(blank_list))
        print(stages[lives])
    else:
        print(f"The {user_guess} is not in the word! You've lost a live!")
        lives -= 1
        print(" ".join(blank_list))
        print(stages[lives])
        pass
    if lives == 0:
        print("You've lost! Correct word was {}".format(secret_word))
        print(stages[lives])
        break
    if "_" not in blank_list:
        print("Congratulations! You guessed the word: " + secret_word)
        break

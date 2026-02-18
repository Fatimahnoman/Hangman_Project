#                                              "Hangman Game"
import random

words = ["Umbrella", "Computer", "SmartPhone", "TeleScope"]
word = random.choice(words).upper()  # Randomly select a word (This happens every time the game starts)
total_chances = 7  # Total chances user has
guessed_word = "-" * len(word)  # Initialize guessed_word with dashes

while total_chances != 0:
    print(guessed_word)  # Show the current guessed word
    letter = input("Guess a Letter: ").upper()  # Take user input and convert it to uppercase

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]
        
        print(f"Correct guess! Current guessed word: {guessed_word}")

        if guessed_word == word:  # If the guessed word is correct, break the loop
            print(f"Congratulations! You Won the Game!!")
            print(f"The Correct Word is: {word}")
            break  # End the game

    else:
        total_chances -= 1  # Deduct a chance if the guess is incorrect
        print("Incorrect Guess!")
        print(f"The Remaining Chances Are: {total_chances}")
        break
else:
    # If chances are over, end the game and show these messages
    print("Game Over!")
    print("You Lose!")
    print(f"The Correct Word is: {word}")
    
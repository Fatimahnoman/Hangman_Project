🎮 Hangman Game (Console-Based)

A classic Hangman Game built using Python, where the player tries to guess a hidden word one letter at a time before running out of attempts.

📌 Features

🎯 Random word selection

🔤 Letter-by-letter guessing

❌ Limited number of incorrect guesses

📊 Display of guessed letters

🧠 Input validation

🏆 Win / Lose conditions

🎨 Optional ASCII Hangman visuals

🛠️ Technologies Used

Python 3

Built-in modules:

random

📂 Project Structure
hangman-game/
│
├── app.py        # Game logic
├── README.md      # Documentation

⚙️ Requirements

Before running this project, make sure you have:

Python 3 installed
👉 https://www.python.org/downloads/

Check installation:

python --version

🚀 How to Run the Game

Clone the repository:

git clone https://github.com/your-username/hangman-game.git


Navigate to the project folder:

cd hangman-game


Run the game:

python main.py

🎮 How to Play

The computer randomly selects a hidden word

You guess one letter at a time

If the letter is correct → it is revealed in the word

If the letter is wrong → you lose one life

You have limited attempts to guess the word

The game ends when:

You guess the word correctly 🎉

Or you run out of attempts 😢

💡 Example Gameplay
Word: _ _ _ _

Guess a letter: a
Correct!

Word: a _ _ _

Guess a letter: z
Wrong! Attempts left: 5

Word: a _ _ _

⚠️ Rules

Only single letters are allowed

Repeated guesses are not counted

Invalid inputs will be rejected

🎯 Game Logic

Random word is selected from a list

A loop runs until the game ends

Correct guesses update the word display

Incorrect guesses reduce attempts

Win when all letters are guessed

🔄 Future Improvements

Difficulty levels (easy / medium / hard)

GUI version using Streamlit / Tkinter

Score tracking system

Categories (animals, fruits, countries, etc.)

Multiplayer mode

👩‍💻 Author: Fatimah Noman

Python Learner 🚀

Exploring Agentic AI 🤖

⭐ Support

If you like this project, give it a ⭐ on GitHub!

📜 License

This project is open-source and free to use.

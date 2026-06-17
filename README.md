# Modern Hangman Game - Python & Pygame

A sleek, modern, and interactive **Hangman Game** built with Python and Pygame. This project has been upgraded from a simple CLI tool to a fully functional **Graphical User Interface (GUI)** version that is mobile-responsive and web-ready.

## 🌟 Features
- **Modern UI**: Clean and professional aesthetics with a Bootstrap-inspired color palette.
- **Virtual Keyboard**: On-screen A-Z buttons for easy play on mobile devices and touchscreens.
- **Dynamic Graphics**: Interactive hangman drawing that builds piece-by-piece.
- **Web-Ready**: Optimized for deployment on GitHub Pages using `pygbag`.
- **Responsive Design**: Works smoothly on both desktop and mobile browsers.
- **Simple & Fun**: A straightforward "Simple UI Game" perfect for quick entertainment.

## 🎮 How to Play
1.  **Objective**: Guess the hidden word one letter at a time before the hangman is fully drawn.
2.  **Input**: Use your **physical keyboard** (Desktop) or click/tap the **virtual keyboard** (Mobile).
3.  **Lives**: You start with 7 lives. Each incorrect guess removes one life.
4.  **Restart**: Once the game ends (Win or Loss), simply click the **RESTART** button or press 'R' to play again with a new word.

## 🛠️ Installation & Local Run
To run the game on your local machine:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Fatimahnoman/Hangman_Project.git
    cd Hangman_Project
    ```
2.  **Install dependencies**:
    ```bash
    pip install pygame
    ```
3.  **Run the game**:
    ```bash
    python main.py
    ```

## 🌐 Web Deployment
This game is compiled into WebAssembly using `pygbag`. To host it on GitHub Pages:
1.  Run `python -m pygbag --build .`
2.  The resulting `index.html` and assets in the root directory are automatically served by GitHub Pages.

---
*Created as part of my Software Development Portfolio.*

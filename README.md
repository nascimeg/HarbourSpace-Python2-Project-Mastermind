# HarbourSpace-Python2-Project-Mastermind
# BETA Project for Python2 class at Harbour.Space - Ogabek's class 

## About This Project
This project is a Python-based digital version of the classic [**Mastermind**](https://www.amazon.es/dp/B00BULNEVK) board game. It was created as part of the Python II course at Harbour.Space University, to practice:
- Functional programming
- Loops and validation
- Working with randomization
- Dictionaries and lists
- Input/output formatting
- Basic game logic
- Integrating an external API using OPENAI_API_KEY
The goal was to recreate the core mechanics of Mastermind inside the terminal while keeping the gameplay intuitive, fun, and user-friendly.


## What Is Mastermind?
Mastermind is a **code-breaking** game where the computer generates a secret sequence of colors, and the player attempts to guess it within a limited number of rounds.
Your Python version includes:
- Automatic generation of a random color password
- Configurable number of rounds
- Input validation
- Feedback for every guess
- Victory and defeat conditions
- Optional: Debug tools for instructors
- Optional: OpenAI-powered helper mode


## Who This Project Was Created For
This project is intended for:
- **Python II students** learning to structure medium-sized programs
- **Instructors** who want a simple but complete game to evaluate
- **Anyone on GitHub** who wants to clone, run, or extend a terminal game
- **People learning functional decomposition and clean code** 
The code is structured so the teacher can easily inspect, enable/disable debugging options, or modify game rules.


## How the Game Works
- The computer generates a hidden password using colors (e.g., `"red green blue yellow"`)
  - Available colors:
  - red 🔴
  - orange 🟠
  - yellow 🟡
  - green 🟢
  - blue 🔵
  - purple 🟣
- The player tries to guess the code in the correct colors and order.
- After each guess, feedback is given:
  - ● Correct color and correct position
  - ○ Correct color but wrong position
- The game ends when:
  - ✔ The player cracks the code
  - ❌ The attempts run out
  - 🚪 The player chooses to quit
Bonus: The game may respond with AI-generated jokes during gameplay.


## Installation & Setup 
To run the project on your own machine, follow the steps below.

### 1. Clone repository 
<pre><code>git clone https://github.com/YOUR-USERNAME/HarbourSpace-Python2-Project-Mastermind.git
cd HarbourSpace-Python2-Project-Mastermind</code></pre>

### 2. Create a Virtual Environment 
<pre><code>python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows</code></pre>

### 3. Isntall Required Dependecies
The game includes external libraries (e.g., `python-dotenv`, `openai`).
Install everything from `requirements.txt`:
<pre><code>```pip install -r requirements.txt```</code></pre>

### 4. Set Up your `.env` File (Very Important)
Because the game uses the OpenAI API to generate jokes, you must create a `.env` file containing your API key.

#### Create the `.env` file:
<pre><code>OPENAI_API_KEY=your_api_key_here</code></pre>

#### How to get your API key:
1. Go to platform.openai.com
2. Log in
3. Navigate to View API Keys
4. Create a new API key
5. Copy it into your `.env` file
⚠️ Do NOT commit your `.env` file to GitHub.
It should always stay local on your computer.

### 5. Run the game
<pre><code>python3 mastermind.py</code></pre>
That’s it — the game launches in your terminal!


## Usability Showcase
placeholder

## Project Structure
<pre><code>project/
│
├── mastermind.py
├── README.md
├── requirements.txt
├── .env (not included — user must create)
└── assets/
    └── gameplay.gif (optional)
</code></pre>

## Credits
Created by Gabriela (aka nascimeg) and Abhi at Harbour.Space University
Python 2 — Ogabek’s class
With help from ChatGPT (for jokes and code explanations s2)
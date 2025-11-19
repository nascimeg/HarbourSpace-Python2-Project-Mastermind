import random
from openai import OpenAI
from IPython.display import Image, display
from dotenv import load_dotenv
import os
load_dotenv()

# --------------------------
# INIT OPENAI CLIENT
# --------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# --------------------------
# CAT GIFS
# --------------------------
celebration_gifs = [
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"
]

sad_gifs = [
    "https://media.giphy.com/media/9J7tdYltWyXIY/giphy.gif",
    "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif",
    "https://media.giphy.com/media/10dU7AN7xsi1I4/giphy.gif"
]

# --------------------------
# OPENAI JOKE FUNCTION
# --------------------------
def tell_joke():
    """Ask OpenAI for 1 short random board-game joke."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You tell short, funny board-game jokes."},
            {"role": "user", "content": "Tell me a random short board-game joke."}
        ],
        max_tokens=50,
        temperature=1.0
    )
    return response.choices[0].message.content.strip()

# --------------------------
# MASTERMIND GAME FUNCTIONS
# --------------------------
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

def generate_code():
    return [random.choice(COLORS) for i in range(4)]

def check_guess(code, guess):
    white_pins = sum(1 for i in range(4) if guess[i] == code[i])

    code_remaining = []
    guess_remaining = []

    for c, g in zip(code, guess):
        if c != g:
            code_remaining.append(c)
            guess_remaining.append(g)

    black_pins = 0
    for g in guess_remaining:
        if g in code_remaining:
            black_pins += 1
            code_remaining.remove(g)

    return white_pins, black_pins

def get_user_input():
    try:
        return input("Enter 4 colors (red/orange/yellow/green/blue/purple), space-separated:\n> ")
    except EOFError:
        print("Jupyter input issue – run the cell again.")
        return ""

# --------------------------
# MAIN GAME LOOP
# --------------------------
def main():
    print("🎯 Welcome to COLOR MASTERMIND!")
    print("Available colors: red, orange, yellow, green, blue, purple")
    print("You have **10 attempts** to guess the secret code!")
    print("Feedback:")
    print("⚪ White pin = correct color + correct position")
    print("⚫ Black pin = correct color, wrong position")
    print("No pin = incorrect color\n")

    code = generate_code()
    attempts = 0

    while attempts < 10:
        print(f"\n🔎 Attempt {attempts + 1}/10")
        guess_str = get_user_input().strip().lower()
        if not guess_str:
            continue

        guess = guess_str.split()

        if len(guess) != 4 or not all(color in COLORS for color in guess):
            print("❌ Invalid guess! Use 4 colors from:", COLORS)
            continue

        attempts += 1

        white_pins, black_pins = check_guess(code, guess)

        print(f"➡ Feedback: ⚪ {white_pins} white pins | ⚫ {black_pins} black pins")

        # ⭐ CALL OPENAI FOR A JOKE
        print("\n🃏 Board-game joke of the round:")
        print("   " + tell_joke())

        if white_pins == 4:
            print("\n🎉 YOU WIN!")
            print("✨ Secret code:", code)
            print(f"🥳 You cracked the code in {attempts} attempts!")

            # Display random celebratory cat GIF
            display(Image(url=random.choice(celebration_gifs)))
            return

    # User lost
    print("\n💀 GAME OVER!")
    print("You used all 10 attempts.")
    print("The secret code was:", code)

    # Display random sad cat GIF
    display(Image(url=random.choice(sad_gifs)))

main()

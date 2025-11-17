import random

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
PASSWORD_LENGTH = 4
MAX_ROUNDS = 10


# ---------------------------------------------------------
# FUNCTION: Generate secret password
# ---------------------------------------------------------
def generate_password():
    return [random.choice(COLORS) for _ in range(PASSWORD_LENGTH)]


# ---------------------------------------------------------
# FUNCTION: Compare guess vs password and generate feedback
# ---------------------------------------------------------
def evaluate_guess(guess, password):
    """
    Returns:
        black_pegs (int): correct color + correct position
        white_pegs (int): correct color + wrong position
    """
    black = sum(g == p for g, p in zip(guess, password))

    # Count occurrences for white pegs
    # Step 1: Filter out the exact matches
    filtered_guess = [g for g, p in zip(guess, password) if g != p]
    filtered_pass = [p for g, p in zip(guess, password) if g != p]

    # Step 2: Count colors in common
    white = 0
    for color in set(filtered_guess):
        white += min(filtered_guess.count(color), filtered_pass.count(color))

    return black, white


# ---------------------------------------------------------
# FUNCTION: Ask the user for a valid guess
# ---------------------------------------------------------
def get_user_guess():
    while True:
        user_input = input(f"Enter your guess (choose {PASSWORD_LENGTH} colors): ").strip().lower()
        guess = user_input.split()

        # Validate guess
        if len(guess) != PASSWORD_LENGTH:
            print(f"❌ You must enter exactly {PASSWORD_LENGTH} colors.")
            continue

        if not all(color in COLORS for color in guess):
            print(f"❌ Invalid color detected. Valid colors: {', '.join(COLORS)}")
            continue

        return guess


# ---------------------------------------------------------
# MAIN GAME LOOP
# ---------------------------------------------------------
def play_game():
    print("\n🎯 WELCOME TO MASTERMIND 🎯")
    print(f"Available colors: {', '.join(COLORS)}")
    print(f"Password length: {PASSWORD_LENGTH}")
    print(f"Max rounds: {MAX_ROUNDS}\n")

    password = generate_password()
    # Uncomment for debugging:
    # print("SECRET:", password)

    for round_num in range(1, MAX_ROUNDS + 1):
        print(f"\n----- Round {round_num} of {MAX_ROUNDS} -----")
        guess = get_user_guess()

        black, white = evaluate_guess(guess, password)

        print(f"Feedback: {black} black peg(s), {white} white peg(s)")

        if black == PASSWORD_LENGTH:
            print("\n🎉 YOU WIN! You cracked the password!")
            return

    print("\n💀 GAME OVER — You ran out of rounds!")
    print(f"The correct password was: {', '.join(password)}")


# ---------------------------------------------------------
# RUN GAME
# ---------------------------------------------------------
if __name__ == "__main__":
    play_game()

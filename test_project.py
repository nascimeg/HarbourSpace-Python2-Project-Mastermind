import random
from openai import OpenAI
from IPython.display import Image, display
from dotenv import load_dotenv # read .env file because we want to keep our API key secret -> for OPENAI_API_KEY 
import os # allws python to read environment variables 
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
joke_prompts = [
    "Tell me a short joke about either board games or colors (red, blue, green, yellow, purple, or orange)",
    "Give me a short 'roses are red, violets are blue' style poem. It can be silly or teasing",
    "Give me a short funny 'roses are red, violets are blue' roast. Keep it playful and light"
]

# because we needed to import something external and Ogabek shared his Open AI key lol 
def tell_joke():
    """Ask Chat for 1 short random joke/poem/roast""" # used """ for docstring in case we need help and to document what this function does, like help(tell_joke)
    
    selected_prompt = random.choice(joke_prompts) # pick a random style of joke 
    
    response = client.chat.completions.create( # saving as response whatever Chat gives me BY creating a chat completion from the user previoulsy accessed 
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You tell short, funny jokes, poems, or roasts"},
            {"role": "user", "content": selected_prompt}
        ],
        max_tokens=50, # short joke so it doesn't break Ogabek's bank 
        temperature=1.0 # because we random 
    )
    return response.choices[0].message.content.strip() # to remove extra spaces/newlines 

# --------------------------
# MASTERMIND GAME FUNCTIONS
# --------------------------
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# I wanted to incorporate dictionaries on the project sice Ogabek thaught us during class :) 
COLOR_EMOJIS = {
    "red": "🔴",
    "orange": "🟠",
    "yellow": "🟡",
    "green": "🟢",
    "blue": "🔵",
    "purple": "🟣"
}

def generate_code():
    """Generates random 4 color passcode frcom Colors available""" 
    return [random.choice(COLORS) for i in range(4)] # generate a random code of 4 colors from the COLORS list (aka, colors available) 

def check_guess(code, guess):
    """Retrives users guess and compares to code, returning white and black pins. Whites if the color and position are correct, and black pins if the color is correct but position is wrong""" 
    white_pins = sum(1 for i in range(4) if guess[i] == code[i]) # summing 1 for each position where the guess matches the code exactly, like guess[0] == code[0], guess[1] == code[1], etc

    # creating lists to hold remaining elements after counting white pins 
    code_remaining = []
    guess_remaining = []

    # creating tuple using zip to pair up code and guess elements, like code[0] with guess[0], code[1] with guess[1], etc. And adding to remaining lists BUT ONLY WHEN THEY DON'T MATCH (matches have been counted as white pins)
    for c, g in zip(code, guess):
        if c != g:
            code_remaining.append(c)
            guess_remaining.append(g)

    # now counting black pins, we are going to do that from the remaining elements only. Black pins start as 0 
    black_pins = 0
    for g in guess_remaining:
        # whenever we identify a color from guess_remaining that is also in code_remaining, we increment black_pins by 1 and remove that color from code_remaining to avoid double counting
        if g in code_remaining:
            black_pins += 1
            code_remaining.remove(g) # imagine that code_remaning has ['blue','red'] and guess_remaining has ['blue','blue'], we count one black pin for the first 'blue' in guess_remaining, and then we remove 'blue' from code_remaining so that the second 'blue' in guess_remaining doesn't get counted again

    return white_pins, black_pins # we will use this to provide the user feedback 

# Honestly, don't know, Chat provided me when my Jupyter notebook was acting out. It works now, so don't touch it 
def get_user_input():
    """Gets user input safely in Jupyter environment, but beats me what the F this does""" 
    try:
        return input("Enter 4 colors (red, orange, yellow, green, blue, purple), separated by space:\n> ")
    except EOFError: 
        print("Jupyter input issue – run the cell again.")
        return ""

# --------------------------
# MAIN GAME LOOP
# --------------------------
def play_game(): # no longer main, because main will be used later on to "control the game session", since it can have multiple rounds without having to restart the kernel
    """Start the game, inform how to play, create loop for up to 10 attempts, provide feedback, and display jokes and gifs""" 
    print("🎯 Welcome to COLOR MASTERMIND!")
    print("Available colors: red 🔴, orange 🟠, yellow 🟡, green 🟢, blue 🔵, purple 🟣")
    print("You have **10 attempts** to guess the secret code!")
    print("Feedback:")
    print("⚪ White pin = correct color + correct position")
    print("⚫ Black pin = correct color, wrong position")
    print("No pin = incorrect color\n")

    code = generate_code()
    # attempts always starts at 0 
    attempts = 0

    # if user reaches 10 attempts and doesn't guess correctly, they lose, otherwise the loop continues until they guess correctly or run out of attempts
    while attempts < 10:
        print(f"\n🔎 Attempt {attempts + 1}/10") # always let the user know which attempt they are on
        guess_str = get_user_input().strip().lower() # getting user input, stripping extra spaces and converting to lowercase 
        
        # in case the user wants to quit the game early
        if guess_str in ["quit", "exit", "end game"]:
            print("\n😢 Thanks for playing! See you next time!") # why you leaving??? come back :( 
            display(Image(url=random.choice(sad_gifs))) # we sad you left 
            return False 
        
        # checking if Ogabek and Vlad are paying attention lol 
        # if guess_str in ["cheat!", "show me the code", "chat gpt help me!"]:
        #     print("🫣 Cheating activated! Here's the secret code:", code)
        #     continue # restart the loop without counting as an attempt]:
        
        if not guess_str:
            continue # if we didn't get any input, restart the loop, otherwise it will try to split something that doesn't exist 

        guess = guess_str.split() # splitting the input string into elements in a list (elements are the colors)

        if len(guess) != 4 or not all(color in COLORS for color in guess): # if the user inputs anything other than 4 colors from the COLORS list, we inform them it's invalid and restart the loop
            print("❌ Invalid guess! Use 4 colors from:", COLORS)
            continue # same as above, restart the loop and do not count as an attempt 

        # Display guess with emojis so it's more visual (I was having trouble finding my guess written mixed with all of the feedback, so this should help) 
        emoji_guess = " ".join(COLOR_EMOJIS[color] for color in guess) # converting each color in the guess to its corresponding emoji and joining them with spaces
        print(f"Your guess: {emoji_guess}")
        
        attempts += 1 # count attempts only if the input is valid 

        white_pins, black_pins = check_guess(code, guess) # getting feedback from the check_guess function and the white and black pins count

        print(f"➡ Feedback: ⚪ {white_pins} white pins | ⚫ {black_pins} black pins")

        # CALL OPENAI FOR A JOKE
        print("\n🃏 Board-game joke of the round:")
        print("   " + tell_joke())

        if white_pins == 4: # only if user guessed all 4 colors in the correct positions, aka had 4 white pins 
            print("\n🎉 YOU WIN!")
            print("✨ Secret code:", code)
            print(f"🥳 You cracked the code in {attempts} attempts!")

            # Display random celebratory cat GIF
            display(Image(url=random.choice(celebration_gifs))) # URL because Image needs a URL to display the image in Jupyter notebook (ask Chat if you think otherwise u.u)
            break # changing from return, because now users can create a new session without restarting the kernel, so this will break only the loop "while attempts < 10:"

    # only runs if loop NOT broken = user lost after 10 attempts and still didn't guess the code
    else: # this else corresponds to the while loop, it runs only if the while loop completes without a break (meaning the user didn't guess the code correctly in 10 attempts)
        print("\n💀 GAME OVER!")
        print("You used all 10 attempts.")
        print("The secret code was:", code) # let's the user know what the code was so they feel dumb 

    # Display random sad cat GIF
    display(Image(url=random.choice(sad_gifs))) 

    # because we want to keep trying this until the input is valid, aka True, aka the input is either "y" or "yes" or "quit" or "exit" or "end game"
    while True: 
        replay = input("\n🔄 Do you want to play again? (yes / quit / end game)\n> ").strip().lower() # strip to remove any extra spaces and lower because I don't have the time to add to the valid replys list all possibilities with lower and upper case characters 
        if replay in ["yes", "y"]: # options to reestart the game in a new round (new passcode and everything)
            return True # restarting the game session, exits the play_game() function and goes back to main() where play_game() is called again
        elif replay in ["quit", "exit", "end game"]: # options to quit the game session entirely 
            print("\n😢 Thanks for playing! See you next time!") # why you leaving??? pls, come back :( 
            display(Image(url=random.choice(sad_gifs))) # we sad you left 
            return False # exits the play_game() function and goes back to main() where play_game() is called again, but now main() will break the loop and end the program
        else: # just because users can type whatever and we need a valid input to proceed 
            print("❌ Invalid input! Please type 'yes' to play again or 'quit' to exit.")   


# --------------------------------------------------
# MAIN GAME CONTROLLER
# --------------------------------------------------
def main(): 
    """Controls full game session + replay loop."""
    # so we allow multiple rounds of the game without restarting the kernel 
    while True: 
        keep_playing = play_game() # play_game() now returns True if user wants to play again, False if they want to quit 
        if not keep_playing:
            break # if they want to quit, it beaks the loop and ends the program 


main()

# Flow summary
# 1. main() starts and enters a loop to control game sessions
# 2. main() calls play_game()
# 3. play_game() runs the Mastermind game logic for one round
# 4. After play_game() ends, it returns True (if user wants to replay
#    or False (if user wants to quit) to main()
# 5. main() checks the return value:
#    - If True, it loops back to step 2 to start a new round
#    - If False, it breaks the loop and ends the program 
#    - If invalid input, it prompts again until valid input is received 

# While playing the game 
# user guesses -> feedback given -> joke told -> check win/loss -> repeat until win/loss -> end round and option to replay or quit

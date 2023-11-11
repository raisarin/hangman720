secret = "apple"

def check_guess(guess):
    guess.lower()
    if guess in secret:
        print(f"Good guess! {guess} is in the word")
    else: 
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    while True: 
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha(): 
            check_guess(guess)
        else: print("Invalid letter. Please, enter a single alphabetical chracter.")

ask_for_input()
import random

class Hangman(): 
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word): 
                if letter == guess: 
                    self.word_guessed[index] = guess
            self.num_letters -= 1
    
    def ask_for_input(self):
        while True: 
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha(): 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!") 
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

            
testing = Hangman(["Apple"])
testing.ask_for_input()
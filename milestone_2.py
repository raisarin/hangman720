import random

word_list = ["Mango", "Banana", "Apple", "Pear", "Dragonfruit"]
print(word_list)

word = random.choices(word_list)
print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")
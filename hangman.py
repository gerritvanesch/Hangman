from random import *
from hangman_img import *

words = open('./words.txt').read().splitlines()
word = words[randrange(0, len(words))]

print("The word is", len(word), "letters long.")

guess = len(word) * "_"

guessed = []

wrong = 0

def findInWord(letter):
	global guess
	start = -1
	loc = word.find(letter, start+1)
	while loc > start:
		guess = guess[:loc] + letter + guess[loc+1:]
		start = loc
		loc = word.find(letter, start+1)
	return start >= 0

while guess != word:
	letter = input("Guess a letter: ")[0].lower()
	if not letter.isalpha():
		print("Please enter a single letter")
	if letter in guessed:
		print("You've already guessed this letter!")
		continue
	guessed.append(letter)
	if findInWord(letter):
		print("You found a letter! So far, you've found:", guess)
	else:
		wrong += 1
		print("Sorry, that letter is not in the word! You've now made", wrong, "wrong", ( "guess." if wrong == 1 else "guesses."), "You have", 6 - wrong, "wrong", ("guess" if wrong == 5 else "guesses"), "left.")
		printImg(wrong)
		if wrong >= 6:
			print("Sorry, you've run out of guesses! The word was:", word)
			break
else:
	print("Congratulations! You've found the word:", guess)
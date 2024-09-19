import sys
from random import randrange
from datetime import datetime as d

difficulty_level = ({'choice': 1, 'diff_lvl': 'EASY', 'chances': 10}, {'choice': 2, 'diff_lvl': 'MEDIUM', 'chances': 5}, {'choice': 3, 'diff_lvl': 'HARD', 'chances': 3})
def rules():
	print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
	print("\nPlease select the difficulty level:")
	for level in difficulty_level:
		print(f"{level['choice']}. {level['diff_lvl']} ({level['chances']} chances)")

def choose_lvl(lvl):
	try:
		lvl = int(lvl)
		found = False
		for level in difficulty_level:
			if int(level['choice']) == int(lvl):
				found = True
				return level['diff_lvl'], level['chances']
		if not found:
			print("Invalid choice. Enter only integer. 1-3")
			return None
	except ValueError:
		print("Invalid choice. Enter only integer. 1-3")
		return None

def get_rand_number()->int:
	return randrange(100)

def check_y_n(val)-> object:
	if val == 'Y' or val == 'N' or val == 'y' or val == 'n':
		return val.upper()
	else:
		print("Enter only Y/N")
		return None

def check_num(val)-> int:
	try:
		num = int(val)
		if num < 100 and num > 0:
			return num
		else:
			print("Select a number between 1 and 100.")
			return None
	except ValueError:
		print("Enter only integer.")
		return None

def main():
	if len(sys.argv) >= 1:
		rules()
		num = get_rand_number()
		choice = None
		result = None
		while not result:
			choice = input("Enter your choice: ")
			result = choose_lvl(choice)
		difficulty, chances = result
		print(f"Great! You have selected the {difficulty} difficulty level. You have {chances} chances to guess.\nLet's start the game!")
		time_start = d.now()
		attempt=0
		while(attempt<chances):				
			attempt+=1
			print(F'Attempt: ({attempt} of {chances})')
			guess = None
			while (not guess):
				guess = check_num(input("Enter your guess: "))
			if int(guess) > num:
				print(f"Incorrect! The number is greater than {guess}.")
			elif int(guess) < num:
				print(f"Incorrect! The number is less than {guess}.")
			elif int(guess) == num:
				print(f"Congratulations! You guessed the correct number in {attempt} attempt(s).")
				print(f"Completed in {d.now() - time_start}")
				break
		play_again = None
		while not play_again:
			play_again = check_y_n(input("Do you want to play again? (Y/N) "))
		if play_again == 'Y':
			main()
		else:
			print("Exiting. Thank you for playing")
	else:
		print("This script can also be used as a module by importing the process_numbers function.")

if __name__ == "__main__":
	main()
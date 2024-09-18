import sys
from random import randrange

difficulty_level = ({'choice': 1, 'diff_lvl': 'EASY', 'chances': 10}, {'choice': 2, 'diff_lvl': 'MEDIUM', 'chances': 5}, {'choice': 3, 'diff_lvl': 'HARD', 'chances': 3})
def rules():
	print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
	print("\nPlease select the difficulty level:")
	for level in difficulty_level:
		print(f"{level['choice']}. {level['diff_lvl']} ({level['chances']} chances)")

def choose_lvl(lvl):
	for level in difficulty_level:
		if int(level['choice']) == int(lvl):
			return level['diff_lvl'], level['chances']
			break

def get_rand_number()->int:
	return randrange(100)


def main():
	# Check if the script is run standalone
	if len(sys.argv) >= 1:
		rules()
		num = get_rand_number()
		choice = input("Enter your choice: ")
		result = choose_lvl(choice)
		print(num)
		if result:
			difficulty, chances = result
			print(f"Great! You have selected the {difficulty} difficulty level. You have {chances} chances to guess.\nLet's start the game!")
			attempt=0
			while(attempt<=chances):				
				attempt+=1
				print(F'{attempt} of {chances}')
				guess = input("Enter your guess: ")
				
				if int(guess) > num:
					print(f"Incorrect! The number is greater than {guess}.")
				elif int(guess) < num:
					print(f"Incorrect! The number is less than {guess}.")
				elif int(guess) == num:
					print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
					break
		else:
			print("Invalid choice")
	else:
		print("This script can also be used as a module by importing the process_numbers function.")

if __name__ == "__main__":
	main()
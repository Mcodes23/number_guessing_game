import random
import time

def play_game():
    print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
''')

    computerChoice = random.randint(1, 100)

    # difficulty selection menu
    print('''
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
''')

    try:
        levelChoice = int(input("Enter your choice: "))
        
        if levelChoice == 1:
            print('''
Great! You have selected the Easy difficulty level.
You have 10 chances to guess the correct number.
Let's start the game!
''')
            chance = 0
            start_time = time.time()  # start time
            while chance < 10:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < computerChoice:
                    print("Too low! Try again.")
                elif guess > computerChoice:
                    print("Too high! Try again.")
                else:
                    end_time = time.time()  # end time
                    time_taken = end_time - start_time  # time taken
                    print(f"Congratulations! You guessed the correct number in {chance + 1} attempts!")
                    print(f"It took you {time_taken:.2f} seconds to guess the correct number.")
                    break
                chance += 1
            if chance == 10:
                print(f"Sorry, you've used all your chances. The correct number was {computerChoice}.")
        
        elif levelChoice == 2:
            print('''
Great! You have selected the Medium difficulty level.
You have 5 chances to guess the correct number.
Let's start the game!
''')
            chance = 0
            start_time = time.time()  # start time
            while chance < 5:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < computerChoice:
                    print("Too low! Try again.")
                elif guess > computerChoice:
                    print("Too high! Try again.")
                else:
                    end_time = time.time()  # end time
                    time_taken = end_time - start_time  # time taken
                    print(f"Congratulations! You guessed the correct number in {chance + 1} attempts!")
                    print(f"It took you {time_taken:.2f} seconds to guess the correct number.")
                    break
                chance += 1
            if chance == 5:
                print(f"Sorry, you've used all your chances. The correct number was {computerChoice}.")
        
        elif levelChoice == 3:
            print('''
Great! You have selected the Hard difficulty level.
You have 3 chances to guess the correct number.
Let's start the game!
''')
            chance = 0
            start_time = time.time()  # start time
            while chance < 3:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < computerChoice:
                    print("Too low! Try again.")
                elif guess > computerChoice:
                    print("Too high! Try again.")
                else:
                    end_time = time.time()  # end time
                    time_taken = end_time - start_time  # time taken
                    print(f"Congratulations! You guessed the correct number in {chance + 1} attempts!")
                    print(f"It took you {time_taken:.2f} seconds to guess the correct number.")
                    break
                chance += 1
            if chance == 3:
                print(f"Sorry, you've used all your chances. The correct number was {computerChoice}.")
        
        else:
            print("Invalid choice, please enter a number between 1 and 3.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main game loop
while True:
    play_game()
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break

import random
import art

def higher_lower():
    print(art.logo)
    print("Welcome to Higher or Lower")
    print("See how far you can make it against the computer.")

    current_number = random.randint(1, 100)
    score = 0
    keep_playing = True

    # Building the game logic
    while keep_playing:
        print(f"Current number: {current_number}")
        guess = input("Will the next number be higher or lower? Type 'H' or 'L': ").lower()

        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")

        # Checking if the guess was correct
        if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
            score += 1
            print(f"You guessed correctly! Nice job and keep going! Your current score is: {score}")
        else:
            print(f"You guessed incorrectly! The correct number was {next_number}")
            print(f"Thanks for playing! Your final score was {score}")
            keep_playing = False

        # Updating the current number to the next number for the next round
        current_number = next_number

        # Asking the user if they'd like to play again after the game ends
        if not keep_playing:
            play_again = input("Would you like to play again? Type 'Y' or 'N': ").lower()
            if play_again == 'y':
                # Reset game state to play again
                current_number = random.randint(1, 100)
                score = 0
                keep_playing = True
            else:
                print(f"Thanks for playing! Your final score was {score}.")
                keep_playing = False

# Start the game
if __name__ == "__main__":
    higher_lower()

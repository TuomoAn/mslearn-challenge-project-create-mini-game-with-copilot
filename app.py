# Write a program that plays Rock, Paper, Scissors

# Import the random module
import random

# Write a main function to handle the game logic
# The main function should:
# Validates the user input and print an error message if the user choice is invalid
# Transform user input to lowercase
# Ask the user to play again
# Display the final score
def main():
    # Initialize variables
    user_score = 0
    computer_score = 0
    play_again = 'y'

    # Display welcome message
    print('Welcome to Rock, Paper, Scissors!')

    # While loop to play the game
    while play_again == 'y':
        # Get user input
        user_choice = input('Please choose rock, paper, or scissors: ')

        # Validate user input
        while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
            print('Invalid input. Please try again.')
            user_choice = input('Please choose rock, paper, or scissors: ')

        # Transform user input to lowercase
        user_choice = user_choice.lower()

        # Generate computer choice
        computer_choice = random.randint(1, 3)

        # Assign computer choice to rock, paper, or scissors
        if computer_choice == 1:
            computer_choice = 'rock'
        elif computer_choice == 2:
            computer_choice = 'paper'
        else:
            computer_choice = 'scissors'

        # Display user and computer choices
        print('You chose ' + user_choice + '.')
        print('The computer chose ' + computer_choice + '.')

        # Determine winner and display results
        if user_choice == computer_choice:
            print('It\'s a tie!')
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('You win!')
            user_score += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('You win!')
            user_score += 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('You win!')
            user_score += 1
        else:
            print('The computer wins!')
            computer_score += 1

        # Ask the user to play again
        play_again = input('Would you like to play again? (y/n): ')

    # Display final score
    print('The final score is:')
    print('You: ' + str(user_score))
    print('Computer: ' + str(computer_score))

# Call the main function
main()
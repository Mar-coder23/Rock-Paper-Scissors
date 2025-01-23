# Creating a Rock Paper Scissors game

# Imported random library to get random number
import random

# Prints this text at start
print("Welcome to Rock, Paper, Scissors")


# assigns both the cpu and user counter to zero to start
cpu_counter = 0
user_counter = 0

# created a random number generator from 1 to 3
def random_selection():
    return str(random.randint(1, 3))
    


# created a function determine_winners with two parameters cpu and user options. This is the code to determine how to win or lose or even tie
def determine_winner(cpu_option, user_option):
    #Had to assign this again as global so it knows to find it outside of function block
    global user_counter, cpu_counter
    
    # If this is true, then print the block code which says you tied 
    if cpu_option == '1' and  user_option == '1' or cpu_option == '2' and user_option == '2' or cpu_option == '3' and user_option == '3':
        print(f"You've tied the Cpu. Score: USER {user_counter} CPU {cpu_counter}")
    # Else if this is true then print the block code which says you win and adds the user counter with a + 1 to increment the score
    elif user_option == '1' and cpu_option =='3' or user_option == '2' and cpu_option == '1' or user_option == '3' and cpu_option == '2':
        user_counter = user_counter + 1
        print(f"You Win! Score: USER {user_counter} CPU {cpu_counter}")
    # Else if this is true then print the block code which says you lose and adds the cpu counter with a + 1 to increment the score
    else:
        cpu_counter = cpu_counter + 1
        print(f"You Lose. Score: USER {user_counter} CPU {cpu_counter}")
    



# created play_game function which is main code to see if user selected a number from 1 to 3, if not then invalid, or q to quit. it also has stored random number for cpu
def play_game():
    # made these variables global so it sees it out of this function
    global user_counter, cpu_counter
    # while the below statements is true, run this block of code continuosly unless specified otherwise
    while True:
        
        # if and else if the cpu or user gets to 10. It will either print you lost or win, and restarts the user and cpu counter back to zero for the next games
        if user_counter == 10:
            print("Congrats! You win the game")
            user_counter = 0
            cpu_counter = 0
        elif cpu_counter == 10:
            print("Game over! Better luck next time")
            user_counter = 0
            cpu_counter = 0
    
        # Asking the user for a option to select 1,2,3 or 'q' to quit the game and exit the while loop
        user_input = input("Pick either 1.Rock, 2.Paper, 3.Scissors. (1/2/3) or 'q' to quit: ")
        
        # if the user input is equal to q, then say final score, and break the loop to quit the game
        if user_input.lower() == 'q':
            print(f"Final Score: USER {user_counter} CPU {cpu_counter}")
            print("Thanks for playing")
            break
        # if user input is not either 1, 2, or 3, then say it's an invalid choice and to select the right ones. then continue the loop after the break
        if user_input not in {'1', '2', '3'}:
            print("Invalid choice. Please select 1, 2, or 3. ")
            continue
        
        # store the cpu option variable to the random number generator
        cpu_option = random_selection()
        
        # Make the choices for 1, 2, and 3 with their outputs in a dictionary. to print if it is a 1 then say you chose rock and cpu chose whatever number since random
        choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
        print(f"You chose {choices[user_input]}, CPU chose {choices[cpu_option]}")
        
        
        # call the determine winner function to determine who won and what to output
        determine_winner(cpu_option, user_input)
        
        
play_game()


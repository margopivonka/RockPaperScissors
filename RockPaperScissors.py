from random import randint



print("Welcome to...")
print("Rock, Paper, Scissors, Shoot!")
print("--------------------")

#create list of possible variables
options = ["Rock", "Paper", "Scissors"]

#make cpu pick random vairable
computer_choice = options[randint(0,2)]

#set player to false
player_choice = False

while player_choice == False:
    player_choice = input("Rock, Paper, Scissors?: ")
    print("--------------------")
    print("The computer chose: ", computer_choice)
    print("--------------------")

    if player_choice == computer_choice:
            print("You Tie!")
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("Computer Wins!")
        else:
            print("You Win!")
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("You Win!")
        else:
            print("Computer Wins!")
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("You Win!")
        else:
            print("Computer Wins!")
    else:
        print("That is not a valid option, please try again.")
player_choice = False
computer_choice = options[randint(0,2)]






#user_input = input("Please select and option: Rock, Paper, or Scissors - ")
#print(user_input)
#
#if user_input != "rock":


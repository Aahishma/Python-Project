total_guess = 0
wins = 0
loss = 0
import random
characters = ["rock", "paper", "scissors", "lizard", "spock"]
computer = characters[random.randint(0,4)]
print(computer)

def valid(text, flag):
    error_message= ""
    while True:
        var = input(error_message + text)
        if flag == "s":
            if var.isalpha()==True:
                break
            else:
               error_message = "This is not valid, "
        elif flag =="i":

            if var.isdigit()==True:
                var = int(var)
                break
            else:
                error_message = user_name + " this is not a number, "

        elif flag == "g":
            if var == "rock" or var == "paper" or var == "scissors" or var ==  "lizard" or var == "spock":
                break
            else:
                error_message = user_name + " this is not valid! "
    return(var)

user_name = valid("What is your name? ", "s")
num_rounds = valid(user_name +" how many rounds do you want? ", "i")

while True:
        while num_rounds > total_guess:
            player = valid(user_name + """ ,What do you want as your character:
             Rock, paper, scissors, lizard or spock """, "g" )
            total_guess = total_guess + 1
            if player == computer:
                print("Draw!")
        #             --------------------------------------------
            elif player == "Rock" or player == "rock":
                if computer == "paper" or computer == "spock" :
                    loss = loss + 1
                    print(' '.join(("You lost", computer, "beats", player)))

                if computer == "scissors" or computer == "lizard":
                    wins = wins + 1
                    print(' '.join(("You win", player, "beats", computer)))

            elif player == "Paper" or player == "paper":
                if computer == "scissors" or computer == "lizard":
                    loss = loss + 1
                    print(' '.join(("You lost", computer, "beats", player)))

                if computer == "rock" or computer == "spock":
                    wins = wins + 1
                    print(' '.join(("You win", player, "beats", computer)))

            elif player == "Scissors" or player == "scissors":
                if computer =="Spock" or computer == "rock":
                    loss = loss + 1
                    print(' '.join(("You lost", computer, " beats ", player)))

                if computer  =="paper" or computer == "lizard":
                    wins = wins + 1
                    print(' '.join(("You win", player, "beats", computer)))

            elif player == "Lizard" or  player =="lizard":
                if computer =="scissors" or computer == "rock":
                    loss = loss + 1
                    print(' '.join(("You lost", computer, "beats", player)))


                if computer  == "paper" or computer == "spock":
                    wins = wins + 1
                    print(' '.join(("You win", player, "beats", computer)))

            elif player == "Spock" or player == "spock":
                if computer == "lizard" or computer == "paper":
                   loss = loss + 1
                   print(' '.join(("You lost", computer, "beats", player)))

                if computer  =="rock" or computer == "scissors":
                    wins = wins + 1
                    print(' '.join(("You win", player, "beats", computer)))

        end_game = input("To exit enter N, to play again enter any key:  ")
        if end_game == 'n' or end_game == 'N':
            print("THANKS FOR PLAYING " + user_name + '!')
            break
        else:
            print("go to input")
        total_guess = 0

def game():
    import random
    print(" Rock\n"
          " Paper\n"
          " Scissors\n")
    user_choice = input("now choose one")
    actions = ["Rock", "Paper", "Scissors"]
    ai_choice = random.choice(actions)
    if user_choice == ai_choice:
        print("ITS A TIE! PLAY AGAIN?")
    elif user_choice == "Rock":
        if ai_choice == "Scissors":
            print("AI CHOOSE", ai_choice, "AND YOUR ROCK SMASHES SCISSORS! YOU WON")
        else:
            print("AI CHOOSE", ai_choice, " AND THE PAPER COVERS YOUR ROCK! YOU LOST!")
    elif user_choice == "Paper":
        if ai_choice == "Rock":
            print("AI CHOOSE", ai_choice, "AND YOUR PAPER COVERS THE ROCK! YOU WON!")
        else:
            print("AI CHOOSE", ai_choice, "AND THE SCISSORS CUTS YOUR PAPER! YOU LOST!")
    elif user_choice == "Scissors":
        if ai_choice == "Paper":
            print("AI CHOOSE", ai_choice, "AND YOUR SCISSORS CUTS THE PAPER! YOU WON!")
        else:
            print("AI CHOOSE", ai_choice, "AND THE ROCK SMASHES THE SCISSORS! YOU LOST!")
    else:
        print("UH OHH! PLEASE CHOOSE ROCK/PAPER/SCISSORS")


game()

while True:
    ques = input("WOULD YOU LIKE TO PLAY AGAIN Y/N?")
    if ques == "y":
        game()
    else:
        print("OKAY! THANKS FOR PLAYING")
        quit()

import random
print("Welcome to the Snake Game")
rounds=int(input("How many rounds do you want to play ?\n"))
options=["s","w","g"]
userscore=0
compscore=0
for roundnum in range(1,rounds+1):
    print(f"Round number is {roundnum}")
    print("Choose:\n 's' for Snake\n 'w' for Water\n 'g' for Gun ")

    userchoice= input("Your choice: ").lower()
    if userchoice not in options:
        print("Invalid input")
        continue
    computerchoice= random.choice(options)
    print(f"Computer chose: {computerchoice}")

    if userchoice==computerchoice:
        print("Its a Draw")
    elif (userchoice== 's' and computerchoice== 'w') or \
         (userchoice=='w' and computerchoice=='g') or \
         (userchoice=='g' and computerchoice=='s'):
        print("You win this round!")
        userscore=+1
    else:
        print("Computer wins the round")
        compscore=+1
    
    print("Game Over")
    print(f"Your Score: {userscore}")
    print(f"Computer's Score: {compscore}")

    if userscore>compscore:
        print("You Won")
    elif compscore>userscore:
        print("Computer Won")
    else:
        print("It's a tie!")

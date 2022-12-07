import random

def play():
    user = input("Enter R - rock P - paper S - scissor : ").lower()
    computer = random.choice(['r','p','s'])
    print("Computer: ",computer)
    print("User : ",user)

    if user == computer:
        return "| IT'S a tie! |"

    def win(user,computer):
        if user == 'r'and computer=='s'or user=='s'and computer=='p'or user=='p'and computer=='r':
            return True

    if win(user,computer):
        return "| YOU won! |"
    print("| YOU lost! |")

print(play())
run = True
while run:
    again = input("If you want to play again: ")
    if again in 'yY':
        play()
    else:
        print("| GOOD GAME! |")
        run = False


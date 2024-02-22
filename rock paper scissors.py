import random

def play():
    user =  input("Choose:'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "Its a Tie"
    
    if win (user, computer):
        return "You WON.."
    
    return "You LOST...."


#User wins here..
def win(user,comp):
    if (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or \
          (user == 'r' and comp == 's'):
        return True
    
print(play())

import random
options = ["r", "p", "s"]

computer_choice = random.choice(options)

while(True):
    user_choice = input("Enter your choice(r for rock, p for paper, s for scissors) :")

    if(user_choice == 'r' and computer_choice == 'r'):
        print('draw')
    if(user_choice == 'p' and computer_choice == 'p'):
        print('draw')
    if(user_choice == 's' and computer_choice == 's'):
        print('draw')
    if(user_choice == 'r' and computer_choice == 'p'):
        print('You lost')
    if(user_choice == 'r' and computer_choice == 's'):
        print('You won')
    if(user_choice == 'p' and computer_choice == 's'):
        print('You lost')
    if(user_choice == 'p' and computer_choice == 'r'):
        print('you won')
    if(user_choice == 's' and computer_choice == 'r'):
        print('you lost')
    if(user_choice == 's' and computer_choice == 'p'):
        print('you won')
    

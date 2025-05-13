import random
a = int(input("Enter lower bound number: "))
b = int(input("Enter Upper bound number: "))

print("A random number has been generated in between ",a, "and", b)

number = random.randint(a,b)

while(True):
    guess = int(input("Guess the number: "))
    if(guess == number):
        print("Hooray you have guessed the number")
        break
    elif(guess < number):
        print("Too Low")
    else:
        print("Too high")

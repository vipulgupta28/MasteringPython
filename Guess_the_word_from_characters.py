import random

words = ["cocomelon", "science", "museum", "wings", "chicken", "india", "dog"]

word = random.choice(words)
size = len(word)

ans = ['_'] * size


while True:
    guess = input("guess the character: ")
    for i in range(size):
        if(word[i]==guess):
            ans[i] = guess
    
    print("Current word: ", " ".join(ans))

    if '_' not in ans:
        print("congo, you have gussed the word")
        break





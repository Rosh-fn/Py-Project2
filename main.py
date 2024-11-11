import random

n = random.randint(1, 100)
a = -1
guesses = 0
while(n != a):
    a = int(input("Enter the number :"))
    if (a>n):
        print("lower number please ")
        guesses += 1
    elif(a<n):
        print("higher number please ")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempt")
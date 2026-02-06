import random

def generate_number():
    return random.randint(1, 10)

def check_guess(secret, guess):
    return secret == guess

print("Welcome to Guess the Number!")

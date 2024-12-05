import random
import string

def welcome_message():
    print("¡Bienvenido al Juego de Adivinar Palabras!")
    print("Intenta adivinar la palabra secreta.")

def get_word_list(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file]
    return words

def select_random_word(word_list):
    return random.choice(word_list)

def get_user_guess():
    while True:
        guess = input("Ingresa tu palabra o letra: ").lower().strip()
        if len(guess) > 0 and all(char in string.ascii_letters for char in guess):
            return guess
        else:
            print("Por favor, ingresa una palabra  o letra válida.")

def check_guess(secret_word, user_guess):
    if user_guess == secret_word:
        return True
    else:
        print("La palabra  o letra no es correcta. Intenta de nuevo.")
        return False

def display_word_progress(secret_word, user_guess):
    progress = []
    for char in secret_word:
        if char in user_guess:
            progress.append(char)
        else:
            progress.append("_")
    print(" ".join(progress))

def play_game():
    welcome_message()
    word_list = get_word_list('palabras.txt')
    secret_word = select_random_word(word_list)
    attempts = 0
    guessed_letters = set()

    while True:
        display_word_progress(secret_word, guessed_letters)
        user_guess = get_user_guess()
        attempts += 1
        guessed_letters.add(user_guess)

        if check_guess(secret_word, user_guess):
            print(f"¡Felicitaciones, has adivinado la palabra secreta '{secret_word}' en {attempts} intentos!")
            break

        if len(guessed_letters) == len(secret_word):
            print(f"Lo siento, no has logrado adivinar la palabra secreta '{secret_word}'.")
            break

play_game()
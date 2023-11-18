#!/usr/bin/env python3
"""Hangman Game"""

def initialize():
    print("Choosing word...")
    return "cat"

def get_letter_from_user(chosen_letters):
    letter = input("Choose a letter > ")
    while len(letter) != 1 or letter in chosen_letters:
        print("Invalid letter")
        letter = input("Choose a letter > ")
    return letter

def is_letter_in_word(letter, word):
    in_word = letter in word
    if in_word:
        print("Letter is in word")
    else:
        print("Letter is not in word")
    return in_word


def print_word(word, identified_letters):
    print()
    for letter in word:
        if letter in identified_letters:
            print(letter, end=' ')
        else:
            print("_", end=' ')
    print("\n\n")


def is_missing_letters(identified_letters, word):
    for letter in word:
        if letter not in identified_letters:
            return True
    return False

def end_game_play(identified_letters, word):
    if is_missing_letters(identified_letters, word):
        print("You lost")
    else:
        print("You won")

def start_game_play(word):
    current_try = 1
    identified_letters = set()
    chosen_letters = set()
    print("Starting game...")
    while current_try <= 6 and is_missing_letters(identified_letters, word):
        print_word(word, identified_letters)
        print("Try number:", current_try)
        letter = get_letter_from_user(chosen_letters)
        chosen_letters.add(letter)
        letter_in_word = is_letter_in_word(letter, word)
        if letter_in_word:
          identified_letters.add(letter)
        current_try += 1
    print_word(word, identified_letters)
    end_game_play(identified_letters, word)


def main():
    print("Welcome to Hangman")
    word = initialize()
    start_game_play(word)

if __name__ == "__main__":
    main()

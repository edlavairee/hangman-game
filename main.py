import random

with open('words.txt') as file:
    words = file.readlines()
    words = [word.strip() for word in words]

selected_word = random.choice(words)

word_creator = []

for letter in selected_word:
    word_creator.append("_")

tries = 5

while "_" in word_creator and tries > 0:

    print(' '.join(word_creator))
    print(f'You have {tries} tries.')

    letter_guessed = input("Enter a letter:")

    if letter_guessed not in selected_word:
        tries -= 1

    if letter_guessed in selected_word:
        for index in range(len(selected_word)):
            if letter_guessed == selected_word[index]:
                word_creator[index] = letter_guessed

    if tries == 0:
        print("Sorry, Game Over!")
        print(f"The word was {selected_word}")

    if tries > 0 and "_" not in word_creator:
        print("You win! The word was:")
        print(''.join(word_creator))

import random
import hangman_art
from hangman_words import words

#UI
print(hangman_art.hangman_logo)

#Randomly choose  a word from list
chosen_word = random.choice(words)

#Calculating lives
lives = 6 

#Take user's guess and generate a list for display
end_of_game = False
display = []
for letter in chosen_word:
    display.append("_")
    
while not end_of_game:
    guess = input("Enter your guess:").lower()
    
#Check for repition in input
    if guess in display:
        print(f"Your guessed letter is {guess} which you have already guessed and is repeated")
    elif guess not in display and guess in chosen_word:
        print(f"Your guessed letter {guess} is correct as it is a part of the word.")
        
#Check if guessed letter is part of the word and add dashes to display list
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
            
#In case the guessed letter is wrong so lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f"Your guessed letter ({guess}) is wrong,it is not a part of the word")
        print(hangman_art.stages[6-lives])
            
#print the updated list
    print(display)
    
#Losing and winning conditions check
    if "_" not in display and lives != 0:
        end_of_game = True
        print("You Win!")

    elif lives == 0:
        print("You Lose.")

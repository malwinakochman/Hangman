import requests
import random
import string

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
word = str(random.choice(words))
sentence = []

#Entering gaps in the array
for letter_of_word in word:
    if letter_of_word == " ":
        sentence.append(" ")
    else:
        sentence.append("_")

class Game():

    def __init__(self):
        self.used_letters = ""

    def letter_guess(self):
        letter = input("Please enter letter\n")
        
        #Checking whether it is a letter or a sign
        counter = 0
        for p in string.ascii_letters:
            if letter == p:
                    counter += 1
        if counter == 0:
            print("It is sign. Please enter letter.")
            letter = input("Please enter letter\n")

        #Checking if the letter has already been used
        for y in self.used_letters:
            if y == letter:
                print("The letter was used. Please enter another letter.")
                letter = input("Please enter letter\n")

        self.used_letters += letter
        counter = 0
        counter2 = 0
        counter3 = 0
        chwilowe = 0

        #Checking how many times it occurs
        for m in word:
            if letter.lower() == m.lower():
                counter2 +=1

        #Writing letters into the array
        while counter3 != counter2:
            for n in word:
                counter += 1
                if letter.lower() == n.lower():
                    counter3 += 1
                    sentence[counter+chwilowe-1] = letter.lower()
                    chwilowe += counter
                    counter = 0
        
                    
        print(*sentence)
        
                 

game = Game()
for tries in range(0,10):
    final_sentence = ""
    for letter_of_sentence in sentence:
        final_sentence += u
    if final_sentence == word:    
            print(f"You won the game. The word is {word}")
            break
    else:
        game.letter_guess()

print(f"All tries have been used. Game over. The word is {word}")



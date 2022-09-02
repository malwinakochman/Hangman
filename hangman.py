import requests
import random
import string

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
word = str(random.choice(words))
haslo = []

#Wpisujemy luki w tabelke
for l in word:
    if l == " ":
        haslo.append(" ")
    else:
        haslo.append("_")

class Game():

    def __init__(self):
        self.used_letters = ""

    def letter_guess(self):
        letter = input("Please enter letter\n")
        
        #Sprawdzamy czy jest literą czy znakiem
        counter = 0
        for p in string.ascii_letters:
            if letter == p:
                    counter += 1
        if counter == 0:
            print("It is sign. Please enter letter.")
            letter = input("Please enter letter\n")

        #Sprawdzamy czy litera juz byla uzyta
        for y in self.used_letters:
            if y == letter:
                print("The letter was used. Please enter another letter.")
                letter = input("Please enter letter\n")

        self.used_letters += letter
        counter = 0
        counter3 = 0
        counter4 = 0
        chwilowe = 0

        #ile razy wystepuje sprawdzamy
        for m in word:
            if letter.lower() == m.lower():
                counter3 +=1

        #wpisujemy do tablicy litery
        while counter4 != counter3:
            for n in word:
                counter += 1
                if letter.lower() == n.lower():
                    counter4 += 1
                    haslo[counter+chwilowe-1] = letter.lower()
                    chwilowe += counter
                    counter = 0
        
                    
        print(*haslo)
        
                 

game = Game()
for tries in range(0,10):
    haslokoncowe = ""
    for u in haslo:
        haslokoncowe += u
    if haslokoncowe == word:    
            print(f"You won the game. The word is {word}")
            break
    else:
        game.letter_guess()

print(f"All tries have been used. Game over. The word is {word}")



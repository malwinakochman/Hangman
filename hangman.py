import requests
import random
import string
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
haslo = []

#word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
#response = requests.get(word_site)
#words = response.content.splitlines()
#word = random.choice(words)
word2 = "zmiana"

for i in range(0, len(word2)):
    haslo.append("_")

class Game():

    def __init__(self):
        self.used_letters = ""
        self.counter = 0

    def letter_guess(self):
        letter = input("Please enter letter\n")
        for y in self.used_letters:
            if y == letter:
                print("The letter was used. Please enter another letter.")
                

        for p in string.ascii_letters:
            if letter != p:
                    self.counter += 1
        if self.counter == 0:
            print("It is sign. Please enter letter.")

        self.used_letters += letter
        counter = 0
        counter3 = 0
        counter4 = 0
        chwilowe = 0

        #ile razy wystepuje sprawdzamy
        for m in word2:
            if letter == m:
                counter3 +=1

        #wpisujemy do tablicy litery
        
        while counter4 != counter3:
            for n in word2:
                counter += 1
                if letter == n:
                    counter4 += 1
                    haslo[counter+chwilowe-1] = letter
                    chwilowe += counter
                    counter = 0
        
        print(*haslo)
                 

game = Game()
for tries in range(0,10):
    game.letter_guess()



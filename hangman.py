import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
#word = str(random.choice(words))
WORD = "zamiana"
BLANK_SYMBOL = "_"
WORDS_DELIMITER = " "
LETTER_INPUT_MESSAGE = "Please enter letter\n"
NOT_LETTER_MESSAGE = "It is sign."
USED_LETTER_MESSAGE = "The letter was used."
MAX_NUMBER_OF_TRIES = 10
VICTORY_MESSAGE = f"You won the game. The word is {WORD}"
GAME_OVER_MESSAGE = f"All tries have been used. Game over. The word is {WORD}"

class Hangman():

    def __init__(self):
        self.used_letters = ""
        self.letter = ""
        self.sentence = []

    def request_an_input(self):
        self.letter = input(LETTER_INPUT_MESSAGE)
        self.request_an_input_if_not_letter()
        self.request_an_input_if_letter_was_used()
        self.used_letters += self.letter

    def generate_blanks(self, word):
        sentence = []
        for letter_of_word in word:
            if letter_of_word == WORDS_DELIMITER:
                sentence.append(self.letter)
            else:
                sentence.append(BLANK_SYMBOL)
        return sentence
        
    def request_an_input_if_not_letter(self):
        if not self.letter.isalpha():
            print(NOT_LETTER_MESSAGE)
            self.request_an_input()
           
    def request_an_input_if_letter_was_used(self):
        for used_letter in self.used_letters:
            if used_letter == self.letter:
                print(USED_LETTER_MESSAGE)
                self.request_an_input()

    def count_letter_occurences(self, word):
        counter = 0
        for letter_of_word in word:
            if self.letter.lower() == letter_of_word.lower():
                counter +=1
        return counter

    def enter_letters_into_sentence(self, word):
        position_in_array = 0
        letter_occurences_in_word_counter = self.count_letter_occurences(word)
        already_entered_letter_counter = 0
        last_entered_letter_index = 0

        while already_entered_letter_counter != letter_occurences_in_word_counter:
            for letter_of_word in word:
                position_in_array += 1
                if self.letter.lower() == letter_of_word.lower():
                    already_entered_letter_counter += 1
                    self.sentence[position_in_array + last_entered_letter_index - 1] = self.letter.lower()
                    last_entered_letter_index += position_in_array
                    position_in_array = 0
        
        print(*self.sentence)

    def play(self, word):
        self.sentence = self.generate_blanks(word)
        for tries in range(0, MAX_NUMBER_OF_TRIES):
            self.request_an_input()
            self.enter_letters_into_sentence(word) 
            final_sentence = ""
            for letter_of_sentence in self.sentence:
                final_sentence += letter_of_sentence
            if final_sentence == word:    
                print(VICTORY_MESSAGE)
                exit()

        print(GAME_OVER_MESSAGE)    


hangman = Hangman()
hangman.play(WORD)            






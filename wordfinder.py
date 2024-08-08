"""Word Finder: finds random words from a dictionary."""
from random import randrange

class WordFinder:
    
    def __init__(self,path):
        """initialize variables, prints num of words read from file"""
        self.path = path
        self.word_list = []
        self.read_words()
        print(len(self.word_list) + ' words read')

    def read_words(self):
        """reads words from file and adds them to word_list list"""
        with open(self.path,'r') as file:
            for line in file:
                self.word_list.append(line.strip())

    def random(self):
        """prints a random word from word_list"""
        print(self.word_list[randrange(len(self.word_list))])


class SpecialWordfinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)

    def word_list_cleaner(self):
        """clears out empty lines and comments from word list"""
        self.word_list = [word for word in self.word_list if word == word.strip() and not word.startswith('#')]
            
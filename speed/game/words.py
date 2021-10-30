from game import constants
import random 
from game.actor import Actor
from game.point import Point
class Word:
    """
    Keeps track of a word and displays it on the screen
    """

    def __init__(self):
        """
        The Class Constructor
        """
        self._list_of_words = []
        super().__init__()
        self.prepare_words()
        #self._list_of_words = []

    def prepare_words(self):
        """
        This method will create the original starting words for the game
        """
        for x in range(constants.STARTING_WORDS):
            word = (random.choice(constants.LIBRARY))
            position = Point(random.randint(0, constants.MAX_X), random.randint(0, constants.MAX_Y / 2))
            velocity = Point(0, 1)
            self.add_word(word, position, velocity)
    
    def add_word(self, word, position, velocity):
        """
        This method will add a new word to the array storing all the words
        """
        words = Actor()
        words.set_text(word)
        words.set_position(position)
        words.set_velocity(velocity)
        self._list_of_words.append(words)

    def remove_word(self, x):
        """
        This will remove a word from the list if the user guesses a correct word
        """
        self._list_of_words.pop(x)

    def new_word(self):
        """
        This will add a new word to the list of words
        """
        word = (random.choice(constants.LIBRARY))
        position = Point(random.randint(0, constants.MAX_X), random.randint(0, constants.MAX_Y / 2))
        velocity = Point(0, 1)
        self.add_word(word, position, velocity)

    def move_words(self):
        """
        This will move all the words down
        """
        count = len(self._list_of_words) - 1
        for n in range(count, -1, -1):
            word = self._list_of_words[n]
            velocity = word.get_velocity()
            word.set_velocity(velocity)
            word.move_next()

    def get_words(self):
        """
        This return the whole list of words
        """
        return self._list_of_words
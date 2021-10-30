from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """A code template for the game buffer. The responsibility of 
    this class is to keep track of the buffer.
    
    Stereotype:
        Information Holder

    Attributes:
        word (string): The textual representation of the word.
        position (Point): Instance of Point
    """

    def __init__(self):
        """The class constructor.
		
          Args:
            self (Buffer): an instance of Actor.
        """
        super().__init__()
        self._word = ""
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._word}")
    
    def empty_word(self):
        # Called when player hits enter reseting the string '_word'
        self._word = ""

    def prep_display(self, letter):
        # Add each letter to the string '_word' and display over the dashes
        self._word += letter
        self.set_text(f"Buffer: {self._word}")

    def get_typed_word(self):
        # Returns '_word' with the letters typed
        return self._word
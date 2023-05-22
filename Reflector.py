from Rotor import *

class Reflector:

    def __init__(self, mapping):
        self.mapping = dict(zip(ALPHABET, mapping))
        
        for x in self.mapping:
            y = self.mapping[x]
            if x != self.mapping[y]:
                raise ValueError("Error {0} , {1} ".format(x, y))
        
    # Translate position index inside mapping
    def translate(self, position_index) -> int:
        x = self.mapping[ALPHABET[position_index]]
        return ALPHABET.index(x)    
    

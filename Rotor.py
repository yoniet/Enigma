import string 

ALPHABET = string.ascii_uppercase

class Rotor:

    TURN_SIZE = len(ALPHABET)

    def __init__(self, mapping, notch, offset_setting=0):
        self.initial_offset = offset_setting
        self.notch = notch
        self.reset()
        self.forward_mapping = dict(zip(self.alphabet, mapping))
        self.reverse_mapping = dict(zip(mapping, self.alphabet))
    
        
    # Re-initialize the rotor 
    def reset(self) -> None:
        self.rotations = 0
        self.alphabet = ALPHABET
        self.rotate(self.initial_offset)
        
    # Rotate the rotor the given number rotation 
    def rotate(self, number_rotation=1) -> int:
        self.alphabet = self.alphabet[number_rotation:] + self.alphabet[:number_rotation]
        self.rotations += number_rotation
        # print(self.rotations)
        return self.rotations
        
    # Encode
    def encipher(self, character) -> str:
        return self.forward_mapping[character]
    
    # Decode
    def decipher(self, character) -> str:
        return self.reverse_mapping[character]
    
    # Translate and resulting position index from alphabet, if is encipher is right rotor otherwise is decipher is left rotor
    def translate(self, position_index, right=True) -> int:
        x = self.alphabet[position_index]
        x = self.encipher(x) if right else self.decipher(x)
        return self.alphabet.index(x)
    
    # Checking for a match
    def check_notch(self) -> bool:
        if self.alphabet[self.rotate() % self.TURN_SIZE] == self.notch:
            return True
        return False
    
    

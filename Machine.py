
from Rotor import *
from Reflector import *



class Machine:

    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector
        
    
    def reset(self) -> None:
        for rotor in self.rotors:
            rotor.reset()
            

    def encipher(self, text) -> str:
        return "".join((self.encipher_char(x) for x in text))
    

    def decipher(self, text) -> str:
        self.reset()
        return self.encipher(text)
    
    
    def encipher_char(self, x):  
        x = x.upper()
        
        # To check if the character is in alphabet
        if x not in ALPHABET:
            return x
        
        # Position of the first rotor
        position_index = ALPHABET.index(x)
       
        
        # For each of the rotor, determine the character in position index
        for rotor in self.rotors:
            position_index = rotor.translate(position_index)

            
        position_index = self.reflector.translate(position_index)
        
        # After we pass reflector we encipher character in reverse
        for rotor in reversed(self.rotors):
            position_index = rotor.translate(position_index, False)
        
    
        # Check if other rotor should be rotated
        for rotor in self.rotors:
            if rotor.rotate() % Rotor.TURN_SIZE != 0 or (not rotor.check_notch()):
                break
        
        # the terminating position index as the input character's enciphering  
        return ALPHABET[position_index]
    
    if __name__ == "__main__":
        pass
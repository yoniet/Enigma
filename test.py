from Rotor import *
from Reflector import *
from Machine import *

r1 = Rotor("VEADTQRWUFZNLHYPXOGKJIMCSB", 'Q', 1)
r2 = Rotor("WNYPVJXTOAMQIZKSRFUHGCEDBL", 'E', 2)
r3 = Rotor("DJYPKQNOZLMGIHFETRVCBXSWAU", 'V', 3)
reflector = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")

machine = Machine([r1, r2, r3], reflector)
x = machine.encipher("The quick brown fox jumps over the lazy dog")

y = machine.decipher(x)

print(x)
print(y)


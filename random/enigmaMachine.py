#%%
#make an input and save it in let
let = input("Enter a letter: ")
#make a list of the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
posInt = alphabet.index(let)
#make a list of the rotors
rotors = [1,1,1]

def convert(posInt = posInt, rotors = rotors):
    for r in rotors:
        posInt = posInt + r
        if rotors[rotors.index(r)] == 26:
            rotors[rotors.index(r)] = 1
        else:
            rotors[rotors.index(r)] = rotors[rotors.index(r)] + 1
    return posInt

for i in range(0,3):
    print(alphabet[convert()])

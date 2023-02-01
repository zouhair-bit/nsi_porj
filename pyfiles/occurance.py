from pyfiles.edit import checker
from pyfiles.comparasion import comparater
import matplotlib.pyplot as plt


alph_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
            }
pers_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
            }


def dict_updater(uptListe):
    #the keys used in the dicts
    alphabet = "abcdefghikjlmnopqrstuvwxyz"
    for i in range (len(alphabet)):
        # we passe by each key using the string "alphabet"
        # to update them using the list created with the percent fonction
        pers_dict[alphabet[i]] = str(uptListe[i])+"%"
    return pers_dict


def percent(values_deci, length):
    #values_pers is the list that will be used in the graph
    values_pers = []
    # we transform the values into % 
    for item in values_deci:
        val = round((item/length)*100, 3)
        values_pers.append(val)
    return values_pers


def drawer(length):
    # we take the keys make turn the into name to put on the horizontal axis
    names = list(alph_dict.keys())
    # and their values into a list so we can turn them into %
    # values_deci is the list with the values in deciaml
    values_deci = list(alph_dict.values())
    print(values_deci)
    #we transform the decimal list into % using the fonction percent
    values = percent(values_deci, length)
    plt.bar(range(len(alph_dict)), values, tick_label=names)
    # we update the dict for the percent to visualize it without the graph
    pers_dict =  dict_updater(values)
    print(pers_dict)
    plt.show()

def reset():
    alph_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
            }
pers_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
            }
def occ():
    file_loc = checker()
    file = open(file_loc, 'r')
    length = 0
    while True:
        # read by character
        char = file.read(1).lower()
        if char in alph_dict:
            alph_dict[char] += 1
            #the length variable is used to chelp calculate the %
            length += 1
        if not char:
            break
    file.close()
    if length == 0:
        print("file is empty")
    else:
        drawer(length)
        print(comparater(alph_dict, length))
        
    reset()

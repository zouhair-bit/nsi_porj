from pyfiles.edit import checker
import matplotlib.pyplot as plt

alph_dict = {"a": 0,
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
def drawer(lenght):
    # we take the keys make turn the into name to put on the horizontal axis
    names = list(alph_dict.keys())
    # and their values into a list so we can turn them into %
    # values_deci is the list with the values in deciaml
    values_deci = list(alph_dict.values())
    #values_pers is the list that will be used in the graph
    values_pers = []
    
    # for item in values_deci:
    #     # avec chaque nombre on le transform en pour
    #     val = round((item/lenght), 3)
    #     values_pers.append(val)
    print(values_deci)
    print(values_pers)
    
    
    plt.bar(range(len(alph_dict)), values_deci, tick_label=names)
    plt.show()

def nombre_lettres():
    file_loc = checker()
    file = open(file_loc, 'r')
    lenght = 0
    while True:
        # read by character
        char = file.read(1).lower()
        if char in alph_dict:
            alph_dict[char] += 1
            lenght += 1
        if not char:
            break
    file.close()
    drawer(lenght)




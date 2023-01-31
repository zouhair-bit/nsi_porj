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

# frequencies were pulled from this site : https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
english = {"a": 8.12,
            "b": 1.49,
            "c": 2.71,
            "d": 4.32,
            "e": 12.02,
            "f": 2.3,
            "g": 2.03,
            "h": 5.92,
            "i": 7.31,
            "j": 0.1,
            "k": 0.69,
            "l": 3.98,
            "m": 2.61,
            "n": 6.95,
            "o": 7.68,
            "p": 1.82,
            "q": 0.11,
            "r": 6.02,
            "s": 6.28,
            "t": 9.1,
            "u": 2.88,
            "v": 1.11,
            "w": 2.09,
            "x": 0.17,
            "y": 2.11,
            "z": 0.07,
            }
# french frequency, I counted accents such as "é" with the same frequency as "e"
# source of values https://www.sttmedia.com/characterfrequency-french
french = {"a": 8.7,
            "b": 0.93,
            "c": 3.16,
            "d": 3.55,
            "e": 17.83,
            "f": 0.96,
            "g": 0.97,
            "h": 1.08,
            "i": 6.94,
            "j": 0.71,
            "k": 0.16,
            "l": 5.68,
            "m": 3.23,
            "n": 6.42,
            "o": 5.35,
            "p": 3.03,
            "q": 0.89,
            "r": 6.43,
            "s": 7.91,
            "t": 7.11,
            "u": 6.14,
            "v": 1.83,
            "w": 0.04,
            "x": 0.42,
            "y": 0.19,
            "z": 0.21,
            }

def language_close (language) :
    sum = 0 # will be the total difference so that we compare with other languages and determine the texts language
    difference = 0
    nombre_lettres()
    extracted_values = list(alph_dict.values) # made lists to use indexes w ma kasser rasse otherwise
    compare_values = list(language.values)
    for i in len(extracted_values):
        difference = abs(extracted_values[i] - compare_values[i])
        sum += difference
def text_language (languageList): # the language list contains the names of all the dictionnaries available
    minimum = 10000
    language = ''
    for i in languageList :
        language_close(i)
        if sum < minimum :
            minimum = sum
            language = i
    return (f"This text is written in {language} as it's the closest in frequency with a {minimum} % divergance")


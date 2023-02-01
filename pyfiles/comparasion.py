# frequencies were pulled from this site : https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
English_dict = {"a": 8.12,
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
French_dict = {"a": 8.7,
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

German_dict = {"a": 6.516,
            "b": 1.886,
            "c": 2.732,
            "d": 5.076,
            "e": 16.396,
            "f": 1.656,
            "g": 3.009,
            "h": 4.577,
            "i": 6.550,
            "j": 0.268,
            "k": 1.417,
            "l": 3.437,
            "m": 2.534,
            "n": 9.776,
            "o": 2.594,
            "p": 0.670,
            "q": 0.018,
            "r": 7.003,
            "s": 7.270,
            "t": 6.154,
            "u": 4.166,
            "v": 0.846,
            "w": 1.921,
            "x": 0.034,
            "y": 0.039,
            "z": 1.134,
            }

Spanish_dict = {"a": 11.525,
            "b": 2.215,
            "c": 4.019,
            "d": 5.010,
            "e": 12.181,
            "f": 0.692,
            "g": 1.768,
            "h": 0.703,
            "i": 6.247,
            "j": 0.493,
            "k": 0.011,
            "l": 4.967,
            "m": 3.157,
            "n": 6.712,
            "o": 8.683,
            "p": 2.510,
            "q": 0.877,
            "r": 8.871,
            "s": 7.977,
            "t": 4.632,
            "u": 2.927,
            "v": 1.138,
            "w": 0.017,
            "x": 0.215,
            "y": 1.008,
            "z": 0.467,
            }

def percent(values_deci, length):
    #values_pers is the list that will be used in the graph
    values_pers = []
    # we transform the values into % 
    for item in values_deci:
        val = round((item/length)*100, 3)
        values_pers.append(val)
    return values_pers

languageList = [French_dict, English_dict, German_dict, Spanish_dict]
languageList_names = ['French', 'English', 'German', 'Spanish']

def comparater(dic, length):
    minimum = 10000
    language = ''
    # we transform the extraced values into %
    values_deci = list(dic.values())
    extracted_values = percent(values_deci, length)
    
# the language list contains the names of all the dictionnaries available
    for i in languageList :
        sum = language_close(i, extracted_values)
        if sum < minimum :
            minimum = sum
            language = i
    index_language = languageList.index(language)
    return (f"This text is written in {languageList_names[index_language]} as it's the closest in frequency with a {round(minimum, 3)} % divergance")

def language_close(language, extracted_values):
    # for each language we turn them into lists to compare them 
    compare_values = list(language.values())
    sum = 0 # will be the total difference so that we compare with other languages and determine the texts language
    difference = 0
    for i in range(len(extracted_values)):
        difference = abs(extracted_values[i] - compare_values[i])
        sum += difference
    return sum
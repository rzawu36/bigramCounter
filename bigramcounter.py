from collections import Counter
import time
from Tkinter import Tk
from tkFileDialog import askopenfilename

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print 'duzina alphabeta je: ' + str(len(alphabet))
print 'alphabet na kvadrat: ' + str(len(alphabet) * len(alphabet))
Tk().withdraw()
filename = askopenfilename()

if filename:
    with open(filename, 'r') as myFile:
        data = myFile.read()




    start = time.time()
    def getBigrams(alphabet):
            temp_list = []
            for x in alphabet:
                for y in alphabet:
                    temp_list.append(x + y)
            return temp_list

    bigrams = getBigrams(alphabet)
    print 'all possible bigrams in alphabet are: ' + str(bigrams)

    def howManyBigramsInString(text):
        possibleBigrams = []
        for char, nextchar in zip(text[::1], text[1::]):
                    possibleBigrams.append(char + nextchar)


        actualBigrams = []
        for item in possibleBigrams:
            for bigram in getBigrams(alphabet):
                if item == bigram:
                    actualBigrams.append(bigram)

        return actualBigrams


    numberOfBigrams = howManyBigramsInString(data.lower())
    print Counter(numberOfBigrams)
    end = time.time()
    minutes = end - start
    seconds = end % minutes
    print 'elapsed time: ' + str(minutes /60) + ':' + str(seconds)
else:
    print 'filename is not chosen'

# nick nazari
# 2019 feb 17
# classifes text chunks by "positive" or "negative" based off of the phrases that they contain

# allows the user to define a list of positive and negative words based off of a text file
# for example, the user might decide that "kill" is a negative word and that "enjoy" is a positive word

import re

class TextChunk:
    def __init__(self, filename):
        with open(filename) as f:
            self.text = f.read()
        self.wordslist = re.sub("[^\w]", " ",  self.text).split() 
        self.pwords = 0
        self.nwords = 0
        self.classification = "unclassified"
        self.plist = []
        self.nlist = []

    def setPlist(self, filename):
        # read positive words from a file
        try:
            with open(filename) as f:
                self.plist = f.read().split('\n')
            return True

        except:
            return False

    def setNlist(self, filename):
        # read negative words from a file 
        try:
            with open(filename) as f:
                self.nlist = f.read().split('\n')
            return True

        except:
            return False

    def classify(self):
        for word in self.wordslist:
            if word in self.plist:
                self.pwords += 1
            elif word in self.nlist:
                self.nwords += 1

            # if word is in neither list, nothing happens. its a neutral word

        if self.pwords > self.nwords:
            self.classification = "positive"
        elif self.pwords < self.nwords:
            self.classification = "negative"
        else:
            self.classification = "neutral"

        return self.classification

if __name__ == "__main__":
    print("[TEST DRIVER EXECUTING]")

    romeo = TextChunk("romeo.txt")
    romeo.setPlist("positive-words.txt")
    romeo.setNlist("negative-words.txt")
    print(romeo.classify())

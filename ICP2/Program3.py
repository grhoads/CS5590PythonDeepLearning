fileName = "Text"
infile = open(fileName,'r')
fileLines = infile.readlines()

for i in fileLines:
    wordList = i.split()
    numWords = 0
    numLetters = 0
    for x in wordList:
        for z in x:
            if z.isupper() or z.islower():
                numLetters += 1
    for n in wordList:
        numWords += 1
    print(i, "---> Words:", numWords, ", letters:", numLetters)

infile.close()

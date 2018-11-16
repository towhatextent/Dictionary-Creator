#Syllable Maker
#Designed for the making of conlangs

import random

#Define a program to "unpack" the actual file, i.e: render it usable
def unpackConsonantFile(consonantFile2):
    #Parse the consonant file by line breaks
    consonantFile2 = consonantFile2.split("\n")

    #Parse each of them by tabs
    #Reassign all the variables to their parsed versions
    for i in range(len(consonantFile2)):
        consonantFile2[i] = consonantFile2[i].split("\t")

        #Parse each sublist by spaces
        for j in range(len(consonantFile2[i])):
            consonantFile2[i][j] = consonantFile2[i][j].split(" ")
    return(consonantFile2)

#Convert the list of all consonants to a regular list of strings
def convertListOfListsToListOfStrings(listOfLists):
    outputList = []
    #Take each element and convert it to a string, then add it to the new list
    for i in range(len(listOfLists)):
        #I put a [0] at the end because this is made for lists of lists in which the second tier of lists contains a single element
        outputList.append(listOfLists[i][0])
    return outputList

#Define a program to create half the shell of a syllable
def createHalfShell(position):
    #Position means onset or coda
    #Check which position
    if position == "onset":
        listOfListsOfUsableConsonants = listOfOnsetFollowers
    elif position == "coda":
        listOfListsOfUsableConsonants = listOfCodaFollowers

    #Number of consonants
    numConsonant = random.randint(0,5)

    #Cluster
    consonantCluster = ""

    #Create cluster
    for i in range(numConsonant):

        #Not whichStart: how about whichOne
        
        #Check if this is the first consonant or if other rules need to be applied
        if i == 0:
            #Store the index of the consonant used in this cycle
            whichOne = random.randint(0,len(listOfConsonants)-1)
            #Create the new consonant
            newConsonant = listOfConsonants[whichOne]
        else:
            #Obtain the proper follower set from the list of lists of consonants using the index of the last value
            whichFollowerSet = listOfListsOfUsableConsonants[whichOne]

            #Get a consonant index from the list of followers
            whichOne = random.randint(0,len(whichFollowerSet)-1)
            #Get a consonant from the follower set
            newConsonant = whichFollowerSet[whichOne]

            #Find the new consonant in the list of consonants to set whichOne to a re-usable value
            whichOne = listOfConsonants.index(newConsonant)
            
        consonantCluster += str(newConsonant)

    return consonantCluster

#Open both files
consonantFileRaw = open("consonantPairFile.txt","r")
nucleusFileRaw = open("vowelsXSAMPA.txt","r")

consonantFile = consonantFileRaw.read()
nucleusFile = nucleusFileRaw.read()

consonantFileRaw.close()
nucleusFileRaw.close()

#Make the consonant file something usable
consonantFile = unpackConsonantFile(consonantFile)

#Assign names to the lists
listOfConsonants = convertListOfListsToListOfStrings(consonantFile[0])
listOfOnsetFollowers = consonantFile[1]
listOfCodaFollowers = consonantFile[2]

#Make the nucleus file something usable
nucleusFile = nucleusFile.split('\n')

#Get number of syllables to generate
numberOfSyllables = 0

#Open output syllable file
outputSyllableFile = open("syllableList.txt","w")

#Request input until the value is acceptable
while numberOfSyllables == 0:
    try:
        numberOfSyllables = int(input("How many syllables?\n"))
    except:
        print("Please type in an integer value.")

#Create as many syllables as requested
for i in range(numberOfSyllables):
    syllable = createHalfShell("onset")+nucleusFile[random.randint(0,len(nucleusFile)-1)]+createHalfShell("coda")

    #Print the syllable
    outputSyllableFile.write(syllable+'\n')
    
#Close output syllable file
outputSyllableFile.close()

#Goodbye!
    
    


#Syllable Maker
#Designed for the making of conlangs

import random

#Define a function to request input
def requestIntegerInput(variable,prompt,minValue):
    while variable < minValue:
        try:
            variable = int(input(prompt+'\n'))
        except:
            print("Please type in a positive integer value.")
    return variable

#Define a program to "unpack" the actual list, i.e: render it usable
def unpackConsonantList(inputConsonantList):
    #Parse the consonant file by line breaks
    inputConsonantList = inputConsonantList.split("\n")

    #Parse each of them by tabs
    #Reassign all the variables to their parsed versions
    for i in range(len(inputConsonantList)):
        inputConsonantList[i] = inputConsonantList[i].split("\t")

        #Parse each sublist by spaces
        for j in range(len(inputConsonantList[i])):
            inputConsonantList[i][j] = inputConsonantList[i][j].split(" ")
    return(inputConsonantList)

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
    if position == 'o':
        listOfListsOfUsableConsonants = listOfOnsetFollowers
    elif position == 'c':
        listOfListsOfUsableConsonants = listOfCodaFollowers

    #Number of consonants
    numConsonant = random.randint(minClusterLength,maxClusterLength)

    #Cluster
    consonantCluster = ""

    #Create cluster
    for i in range(numConsonant):

        #Not whichStart: how about whichOne
        
        #Check if this is the first consonant or if other rules need to be applied
        if i == 0:
            newConsonant = ''
            #Prevents empty strings
            while newConsonant not in listOfConsonants:
                #Store the index of the consonant used in this cycle
                whichOne = random.randint(0,len(listOfConsonants)-1)
                #Create the new consonant
                newConsonant = listOfConsonants[whichOne]
        else:
            #Obtain the proper follower set from the list of lists of consonants using the index of the last value
            whichFollowerSet = listOfListsOfUsableConsonants[whichOne]

            newConsonant = ''
            
            #Prevents empty strings
            while newConsonant not in listOfConsonants:
                #Get a consonant index from the list of followers
                whichOne = random.randint(0,len(whichFollowerSet)-1)
                #Get a consonant from the follower set
                newConsonant = whichFollowerSet[whichOne]


            #Find the new consonant in the list of consonants to set whichOne to a re-usable value
            whichOne = listOfConsonants.index(newConsonant)
            
        consonantCluster += str(newConsonant)

    return consonantCluster

#Define subprogram to turn list into string
def convertListToString(inputList):
    outputString = ''
    #Append every element to an empty string
    for i in range(len(inputList)):
        outputString = outputString + inputList[i]
        #Check if it's the last one
        if i != len(inputList)-1:
             outputString = outputString + '\n'
            
    return outputString


#Open both files
consonantFile = open("consonantPairFile.txt","r")
nucleusFile = open("vowelsXSAMPA.txt","r")

consonantList = consonantFile.read()
nucleusList = nucleusFile.read()

consonantFile.close()
nucleusFile.close()

#Make the consonant list something usable
consonantList = unpackConsonantList(consonantList)

#Assign names to the lists
listOfConsonants = convertListOfListsToListOfStrings(consonantList[0])
listOfOnsetFollowers = consonantList[1]
listOfCodaFollowers = consonantList[2]

#Make the nucleus list something usable
nucleusList = nucleusList.split('\n')

#Get number of syllables to generate
numberOfSyllables = -1
minClusterLength = -1
maxClusterLength = -1

numberOfSyllables = requestIntegerInput(numberOfSyllables,'How many syllables?',1)
minClusterLength = requestIntegerInput(minClusterLength,'How short should the clusters be, minimum?',0)
maxClusterLength = requestIntegerInput(maxClusterLength,'How long should the clusters be, maximum?',0)

syllableList = []

#Create as many syllables as requested
for i in range(numberOfSyllables):
    #Hopefully this way the program thinks it's in the file.
    numberOfInstancesOfSyllable = 1

    counter = 0

    syllable = ''

    #Create a new syllable until it is unique
    while numberOfInstancesOfSyllable >= 1 and counter <= 10:
        onset = createHalfShell('o')
        nucleus = nucleusList[random.randint(0,len(nucleusList)-1)]
        coda = createHalfShell('c')
        
        syllable = onset + nucleus + coda

        numberOfInstancesOfSyllable = syllableList.count(syllable)

        counter += 1

    #If syllable is not empty, add the syllable to the list
    if syllable != '':
        syllableList.append(syllable)

syllableList = convertListToString(syllableList)

#Output to file
outputSyllableFile = open("syllableList.txt","w+")
outputSyllableFile.write(syllableList)
outputSyllableFile.close()

#Goodbye!
    
    


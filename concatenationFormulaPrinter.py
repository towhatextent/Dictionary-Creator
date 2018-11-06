# Concatenation Formula Printer (Spreadsheet)
# Prints the concatenation formula used to group the consonants allowed to follow other consonnats in one cell

#Create the string
mainOutput = "=CONCATENATE("

numConsonants = 5
testedValue = '"C"'

#Concatenate for each consonant
for i in range(numConsonants):
    #65 is A's value in the ASCII table
    column = str(chr(i+65))

    row = str(i+2)

    addToOutput = 'IF(OR(Consonants!A'+row+'="A",Consonants!A'+row+'='+testedValue+'),CONCATENATE(Consonants!$'+column+'1," "),"")'

    #If this is the last addition, add the final bracket
    if i == numConsonants - 1:
        addToOutput = addToOutput + ")"
    else:
        addToOutput = addToOutput + ","

    mainOutput = mainOutput + addToOutput

print(mainOutput)

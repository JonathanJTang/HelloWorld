'''
Text Message Translator

Based on a dictionary of slang expressions used in text messages,
this program translates text messages and replaces slang expressions
with their full written equivalent expression.

Created on December 14, 2016
@author: Jonathan Tang
'''

import csv
import string

def removeSomePunct(s):
    """Removes punctuation not used in any slang expressions;
        may need to be revised if new slang expressions are added"""
    punctuation = '""!%&''*+-.;?@[]\\^_`{}~|'
    sSansPunct = ""
    for letter in s:
        if letter not in punctuation:
            sSansPunct += letter
        elif s.find(letter) != 0 and s.find(letter) != len(s)-1:
            #if the punctuation mark is in the middle of the string, replace with a space:
            sSansPunct += " "
        #Do nothing if the punctuation mark is at the ends of the string
    return sSansPunct

def createDictionary(fileName):
    """Creates and returns a dictionary from a .txt file in csv format"""
    dictionary = {}
    with open(fileName,"r") as csvFile:
        fileData = csv.reader(csvFile)  #delimiter = ','
        for row in fileData:
            dictionary[row[0]] = row[1]
    csvFile.close()
    return dictionary

def textTranslateV1():
    """Doesn't fully work"""
    messageCopy = message.split()
    translatedMessage = message

    for word in messageCopy:
        wordFormatted = removeSomePunct(word)
        if wordFormatted.lower in slang.keys():
            translatedMessage = translatedMessage.replace(wordFormatted, slang[wordFormatted.lower()])

    return translatedMessage

def textTranslateV2(message):
    """Uses global variable slang (a dict object)"""
    translatedMessage = ""

    # "Segment" defined as a string of continuous characters without whitespace
    # (may include punctuation)
    for segment in message.split():
        segmentFormatted = ""
        punct = False

        #Adds space(s) to help identify dictionary keys & punctuation marks later
        for letter in segment:
            if letter in "<:=":  #Add a space before certain characters
                segmentFormatted += " "
                punct = True
            elif letter in string.punctuation and punct == False:
                #Only add a space before the first of a series of punctuation marks
                segmentFormatted += " "
                punct = True
            elif letter not in string.punctuation:
                punct = False
            segmentFormatted += letter
        #print(segmentFormatted)

        #Piece together the translated message
        for word in segmentFormatted.split():
            wordSansPunct = removeSomePunct(word)
            #Determines if any parts of the message needs to be replaced
            if wordSansPunct.lower() in slang.keys():
                if word[0] in string.punctuation:
                    translatedMessage = translatedMessage[:len(translatedMessage)-1] #remove space before punctuation
                if wordSansPunct[0] >= "A" and wordSansPunct[0] <= "Z": #Capitalize replacement phrase if orig in text message is capitalized
                    translatedMessage += word.replace(wordSansPunct, slang[wordSansPunct.lower()].capitalize())
                else:
                    translatedMessage += word.replace(wordSansPunct, slang[wordSansPunct.lower()])
            elif word in slang.keys(): #To detect complex punctuation keys
                translatedMessage += word.replace(word, slang[word])
            elif word[0] in string.punctuation:
                translatedMessage = translatedMessage[:len(translatedMessage)-1] #remove space before punctuation
                translatedMessage += word
            else:
                translatedMessage += word
            translatedMessage += " " #add a space after each word

    return translatedMessage


def main():
    global slang
    slang = createDictionary("slang.txt")
    #print(slang)
    exit = False
    print("Jonathan's Text Message Translator")

    while exit == False: #Loop until user wishes to quit
        messageOrig = input("\nPlease enter your message to be translated:\n")

        print("\nThe translated message is:\n",textTranslateV2(messageOrig),"\n")

        answer = input("Do you wish to continue (Enter 'y' or 'n')? ")
        if answer.lower() == 'n':
            exit = True

main()
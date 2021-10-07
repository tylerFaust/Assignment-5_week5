########################################################################
##
## CS 101 Lab
## Program #4?
## Name: Tyler Faust
## Email: tefqhg@umsystem.edu
##
## PROBLEM : Write a program to validate library cards.
##      
## ALGORITHM : 
##      1. take user's input (string of 10 characters)
##      2. Check every part of the string to make sure it is valid
##      3. Return False if invalid, otherwise True.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      I had trouble with the len() and string indexes.
##      I could use len() and compute indexes in the main function,
##      but I could not in the functions. It would give me an error.
##      It would say "card has no length" when card literally
##      does have a length (card is one of the first things defined)
##
########################################################################

import string

#def get_school(string):
    #return string

#def get_grade(string):
    #return string

def character_value(character):
    return ord(character)

def get_check_digit():
    return int((character_value(realFirstChar) + character_value(firstChar)*2 + character_value(secondChar)*3 + character_value(thirdChar)*4 + character_value(fourthChar)*5 + int(fifthChar) + int(sixthChar) + int(seventhChar) + int(eigthChar))) % 10

def verify_check_digit():
    if not substring1.isupper(): #check if first 5 are letters (I use .isupper() because it will return false if there are no letters.)
        return False,"The first 5 characters must be A-Z"
    elif substring2.isupper(): #check if last 3 are 0-9
        return False,"The last 3 characters must be 0-9"
    elif int(ninthChar) != get_check_digit(): #check if last digit is correct
        return False,"Check Digit 10 does not match calculated value {}.".format(get_check_digit()) 
    else: #should be safe to pass as valid
        return True,"" 

if __name__ == "__main__":
    print("{:^50}\n{:^50}".format("Linda Hall","Library Card Check"))
    print("{:^50}".format("=================================================="))
    loop = True
    while loop:
        card = input("Enter Library Card. Hit Enter to Exit ==> ").upper()
        length = len(card)
        if len(card) > 0:
            if length != 10: #check if its long enough
                print("Library card is invalid.\nThe length of the number given must be 10")
            else:
                substring1 = card[0:5]
                substring2 = card[7:10]
                realFirstChar = card[0]
                firstChar = card[1]
                secondChar = card[2]
                thirdChar = card[3]
                fourthChar = card[4]
                fifthChar = card[5] #for some reason, I have to create variables for indexes of card.
                sixthChar = card[6] #if I try to use the index directly, I get an error.
                seventhChar = card[7]
                eigthChar = card[8]
                ninthChar = card[9] #I have no idea why it happens. It doesn't make any sense to me.
                try:
                    fifthChar = int(fifthChar) #using try so the program doesnt error out
                    y = True
                except:
                    y = False
                try:
                    sixthChar = int(sixthChar)
                    z = True
                except:
                    z = False
                
                alerr = False #already errored variable, so only 1 error prints
                if y:
                    if not (1 <= int(fifthChar) or int(fifthChar) <= 3): #check if index 5 is 1-3
                        print(False,", The sixth character must be 1 2 or 3")
                        alerr = True
                elif not y:
                    print(False,", The sixth character must be 1 2 or 3")
                    alerr = True
                if z and not alerr: 
                    if not (1 <= int(sixthChar) or int(sixthChar) <= 4): #check if index 6 is 1-4
                        print(False,", The seventh character must be 1 2 3 or 4")
                elif not z and not alerr:
                    print(False,", The seventh character must be 1 2 3 or 4")
                if z and y: 
                    print(verify_check_digit()) #make it all uppercase
        else:
            loop = False
import sys

# ============== EMAIL VERIFICATION SECTION ============= #

# Verify that there is a '@' symbol present
def verifyAtSymbol(string):
    stringLength = len(string) - 1
    while (stringLength >= 0):
        if (string[stringLength] == '@'):
            return True
        stringLength -= 1
    return False

# Check to make sure '.' symbol is present at least once
# There cannot be 2 consecutive '.' symbols in a row
def verifyDotSymbol(string):
    count = 0
    stringLength = len(string) - 1
    while (stringLength >= 0):
        if (string[stringLength] == '.'):
            count += 1
            if (string[stringLength - 1] == '.'):
                return False
        stringLength -= 1
    return count >= 1
     
# Check to make sure domain is equal to or less than 3 characters
def verifyDomain(string):
    domain = string.rsplit('.', 1)
    return 0 < len(domain[1]) <= 3

# Check to make sure that the following format doesn't pass: .@. OR @@
def verifyContent(string):
    stringLength = len(string) - 1
    while (stringLength >= 0):
        if (string[stringLength] == '@' and string[stringLength - 1] == '.' and string[stringLength + 1] == '.'):            
            return False
        if (string[stringLength] == '@' and string[stringLength - 1] == '@') and stringLength != 0:
            return False  
        stringLength -= 1
    return True

def email_verifier():
    while True:
        enteredEmail = str(input('Enter e-mail to be verified: '))
        
        if verifyAtSymbol(enteredEmail) and verifyDotSymbol(enteredEmail) and verifyDomain(enteredEmail) and verifyContent(enteredEmail):
            print(enteredEmail, "is a Valid Email\n")
        else:
            print(enteredEmail, "is an Invalid Email\n")
            
        print("Would you like to verify another email address?")
        emailMenu = input ("Enter 'y' for yes, otherwise enter anything else to return to the main menu: ")
        
        if (emailMenu != 'y'):
            break

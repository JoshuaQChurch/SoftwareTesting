def verifyDomain(string):
    domain = string.rsplit('.', 1)
    return domain[1]

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

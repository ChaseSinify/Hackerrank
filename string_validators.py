if __name__ == '__main__':
    s = input()
    alphanumericFlag = False
    alphabeticalFlag = False
    digitFlag = False
    lowerFlag = False
    upperFlag = False

    for c in s:
        if c.isalnum():
            alphanumericFlag = True
        if c.isalpha():
            alphabeticalFlag = True
        if c.isdigit():
            digitFlag = True
        if c.islower():
            lowerFlag = True
        if c.isupper():
            upperFlag = True
    
    print(True if alphanumericFlag else False)
    print(True if alphabeticalFlag else False)
    print(True if digitFlag else False)
    print(True if lowerFlag else False)
    print(True if upperFlag else False)

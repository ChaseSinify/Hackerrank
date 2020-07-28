def swap_case(s):
    swapped = [] 
    for c in s:
        if c.islower():
            swapped.append(c.upper())
        elif c.isupper():
            swapped.append(c.lower())
        else:
            swapped.append(c)
    return "".join(swapped)
    #return s.swapcase() 

    


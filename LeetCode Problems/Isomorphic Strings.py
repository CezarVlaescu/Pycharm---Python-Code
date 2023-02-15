def isIsomorphic(string, target):
    if len(string) == 3:
        return len(set(string)) == len(set(zip(string, target))) == len(set(target))
    else:
        return "The string is too length"

print(isIsomorphic('Poo', 'Suo'))

import string

def getTranslatedMessage(key):
    translated = ""
    base = string.ascii_uppercase + string.ascii_lowercase
    for symbol in base:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    values = [ch for ch in translated]
    keys = [ch for ch in base]
    return dict(zip(keys, values))


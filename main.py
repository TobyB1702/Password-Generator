import random
import string


def randomStringGenerator(lengthOfString):
    word = ''.join(
        [random.choice(parametersForString(True, False, False, False)) for n in range(lengthOfString)])
    return word


def parametersForString(asciiLettersLower, asciiLettersUpper, digits, punctuation):
    myWord = ""
    if asciiLettersLower:
        myWord += string.ascii_lowercase

    if asciiLettersUpper:
        myWord += string.ascii_uppercase

    if digits:
        myWord += string.digits

    if punctuation:
        myWord += string.punctuation

    return myWord


print(randomStringGenerator(100))

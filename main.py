import random
import string


def randomStringGenerator(lengthOfString):
    word = ''.join(
        [random.choice(parametersForString(True, False, False)) for n in range(lengthOfString)])
    return word


def parametersForString(asciiLetters, digits, punctuation):
    myWord = ""
    if asciiLetters:
        myWord += string.ascii_letters
    if digits:
        myWord += string.digits
    if punctuation:
        myWord += string.punctuation

    return myWord


print(randomStringGenerator(100))

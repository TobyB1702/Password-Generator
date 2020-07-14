import random
import string

class Backend:
    def randomStringGenerator(self, lengthOfString):
        get = Backend()
        word = ''.join(
            [random.choice(get.parametersForString(True, False, False, False)) for n in range(lengthOfString)])
        return word

    def parametersForString(self, asciiLettersLower, asciiLettersUpper, digits, punctuation):
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

test = Backend()
print(test.randomStringGenerator(100))


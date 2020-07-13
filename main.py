import random
import string

def randomStringGenerator(lengthOfString):
    word = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(lengthOfString)])
    return word

print(randomStringGenerator(100))
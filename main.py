import random
import string

number = random.randint(0,100)
letters = string.ascii_letters
symbols = string.punctuation
randomword = random.choice(letters)

random = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(12)])
print(random)
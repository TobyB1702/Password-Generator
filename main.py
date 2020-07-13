import random
import string

number = random.randint(0,100);
letters = string.ascii_letters;
randomword = random.choice(letters)

print(randomword)
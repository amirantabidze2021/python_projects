import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
   
    ambiguous_chars = '!@#$%^&*...'
    for char in ambiguous_chars:
        characters = characters.replace(char, '')

    
    password = ''.join(random.choices(characters, k=length))
    
    return password


print(generate_password(8))

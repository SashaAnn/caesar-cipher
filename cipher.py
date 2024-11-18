abc = 'abcdefghijklmnopqrstuvwxyz'

shift = 5
plain_text = input('Please enter a sentence:')
plain_text = plain_text.lower()

print(f'The encrypted sentence is: ')
secret_text = ''

for char in plain_text:
    if char in abc:
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
    secret_text += char

print(secret_text)
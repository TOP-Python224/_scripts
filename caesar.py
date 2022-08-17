from string import ascii_lowercase as alc

r = range(1, 27)
alphabet = dict(zip(r, alc))
alphabet_inv = {}
for ordnum, letter in alphabet.items():
    alphabet_inv[letter] = ordnum


while True:
    text = input('\nenter word > ').lower()
    if not text:
        break
    shift = int(input('enter shift > '))
    cypher = ''
    for char in text:
        ordnum = alphabet_inv[char]
        if (res_ordnum := ordnum+shift) > 26:
            cypher += alphabet[ordnum+shift-26]
        else:
            cypher += alphabet[ordnum+shift]
    print(cypher)

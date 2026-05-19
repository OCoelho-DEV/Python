UPPERCASE_RANGE = range(65, 91)
LOWERCASE_RANGE = range(97, 123)
LOWER_Z_LIMIT = ord("z")
UPPER_Z_LIMIT = ord("Z")
UPPER_A_LIMIT = ord("A")
LOWER_A_LIMIT = ord("a")
ALPHABET_SIZE = 26
def caesar(ASCII_unicode: int, shift: int):
    new_code = ASCII_unicode + shift

    if ASCII_unicode not in UPPERCASE_RANGE and ASCII_unicode not in LOWERCASE_RANGE:
        return chr(ASCII_unicode)
    
    if shift >= 0:
        if ASCII_unicode in UPPERCASE_RANGE and new_code > UPPER_Z_LIMIT:
            ASCII_unicode -= ALPHABET_SIZE

        if ASCII_unicode in  LOWERCASE_RANGE and new_code > LOWER_Z_LIMIT:
            ASCII_unicode -= ALPHABET_SIZE
    
    if shift < 0:
        if ASCII_unicode in UPPERCASE_RANGE and new_code < UPPER_A_LIMIT:
            ASCII_unicode += ALPHABET_SIZE

        if ASCII_unicode in  LOWERCASE_RANGE and new_code < LOWER_A_LIMIT:
            ASCII_unicode += ALPHABET_SIZE
    
    return chr(new_code)

def encrypt(word: str, shift: int):
    new_word = ''
    for letter in word:
        code = ord(letter)
        new_letter = caesar(code, shift)
        new_word += new_letter
    return new_word

def decrypt(encrypted: str, shift: int):
    shift = -shift if shift >= 0 else shift
    new_word = ''
    for letter in encrypted:
        code = ord(letter)
        new_letter = caesar(code, shift)
        new_word += new_letter
    return new_word


word = input("Word: ")
shift = int(input("Shift: "))
encrypted = encrypt(word, shift)
print(encrypted)
decrypted = decrypt(encrypted, shift)
print(decrypted)

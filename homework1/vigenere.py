def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    while len(plaintext) > len(keyword):
        keyword += keyword
    while len(keyword) > len(plaintext):
        keyword = keyword[:-1]
    for i in range(0, len(plaintext)):
        if((plaintext[i] in a) or (plaintext[i] in b)):
            if keyword[i] in a:
                if ord(plaintext[i]) + a.index(keyword[i]) > 122:
                    ciphertext += chr(ord(plaintext[i])+a.index(keyword[i])-26)
                else:
                    ciphertext += chr(ord(plaintext[i]) + a.index(keyword[i]))
            if keyword[i] in b:
                if ord(plaintext[i]) + b.index(d[i]) > 90:
                    ciphertext += chr(ord(plaintext[i])+b.index(keyword[i])-26)
                else:
                    ciphertext += chr(ord(plaintext[i]) + b.index(keyword[i]))
            else:
                ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    while len(ciphertext) > len(keyword):
        keyword += keyword
    while len(keyword) > len(ciphertext):
        keyword = keyword[:-1]
    for i in range(0, len(ciphertext)):
        if((ciphertext[i] in a) or (ciphertext[i] in b)):
            if keyword[i] in a:
                if ord(ciphertext[i]) + a.index(keyword[i]) < 97:
                    plaintext += chr(ord(ciphertext[i])-a.index(keyword[i])+26)
                else:
                    plaintext += chr(ord(ciphertext[i]) - a.index(keyword[i]))
            if keyword[i] in b:
                if ord(ciphertext[i]) + b.index(d[i]) < 65:
                    plaintext += chr(ord(ciphertext[i])-b.index(keyword[i])+26)
                else:
                    plaintext += chr(ord(ciphertext[i]) - b.index(keyword[i]))
            else:
                plaintext += ciphertext[i]

    return plaintext


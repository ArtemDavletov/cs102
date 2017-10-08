def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """

    ciphertext = ''
    for i in range(0, len(plaintext)):
        if((65 <= ord(plaintext[i]) <= 87)or(97 <= ord(plaintext[i]) <= 119)):
            ciphertext += chr(ord(a[i]) + 3)
        elif((87 < ord(plaintext[i]) < 91)or(119 < ord(plaintext[i]) < 123)):
            ciphertext += chr(ord(plaintext[i])-23)

    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """

    plaintext = ''
    for i in range(0, len(ciphertext)):
        if((68 <= ord(ciphertext[i]) <= 90) or (100 <= ord(a[i]) <= 122)):
            plaintext += chr(ord(ciphertext[i])-3)
        elif((64 < ord(ciphertext[i]) < 68)or(96 < ord(ciphertext[i]) <= 99)):
            plaintext += chr(ord(ciphertext[i])+23)
    return plaintext


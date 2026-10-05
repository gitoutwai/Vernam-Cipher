from random import randint

def encrypt(msg):
    key = ""
    for _ in range(len(msg)):
        key += (chr(randint(97,122)))

    CipherText = ""
    for charPos in range(len(msg)):
        binChar = bin(ord(msg[charPos]))
        binKeyChar = bin(ord(key[charPos]))

        binFinal = ""
        for bitPos in range(2, len(binChar)):
            if not binChar[bitPos] == binKeyChar[bitPos]:
                binFinal += "1"
            else:
                binFinal += "0"

        FinalCharIndex = int(binFinal, 2)
        FinalCharIndex += 97
        while FinalCharIndex > 122:
            FinalCharIndex -= 26

        CipherText += chr(FinalCharIndex)

    return (CipherText, key)

if __name__ == "__main__":
    message = input().lower()
    cipherText, key = encrypt(message)

    print(cipherText, key)
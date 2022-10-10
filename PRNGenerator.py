import random
import time
import sys

def Encrypt(UserInput):
    #Seed
    x = time.time()
    random.seed(int(x))

    encodedString = UserInput.encode()
    theByteArray = bytearray(encodedString)

    PRN = random.randbytes(len(UserInput))

    CipherOutput = bytes(a ^ b for a, b in zip(theByteArray, PRN))

    print("Seed: ", x, "\n")
    print("Pseudo-Random Sequence: ", PRN, "\n")
    print("Output Byte: ",CipherOutput, "\n")

    Decrypt(CipherOutput, PRN)

    return None

def Decrypt(Cipher,Key):
    plainText = [chr(a ^ b) for (a, b) in zip(Cipher, Key)]
    #print(plainText)
    print("Message Decoded ",''.join(plainText))


if __name__ == "__main__":
    #Accept string message to be encrypted/decrypted
    if len(sys.argv) == 2:
        Encrypt(sys.argv[1])


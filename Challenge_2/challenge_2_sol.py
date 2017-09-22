"""
OSS Challenge #2 - Vignere Cipher Solution
Anthony Nguyen
9/21/17

Explanation
------------
What we know:
 - Vignere Cipher.
 - Key is a 4 letter word.
 - Key is a word in the dictionary.

Pseudo-Code
-----------
open dictionary file.

for each four letter word in the dictionary
  Attempt to decrypt the cipher text with the four letter word.
    If the results of the decryption are words from teh dictionary
        Store the key in a text and store the plain text in the text.

"""
CIPHER_TEXT = "vp fulp go xcvne jbul ziafevny"
KEY = "ulna"

def decryptVignere(message, key):
    '''
    Decrypt the vignere cipher using the specified key.
    Source: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Algebraic_description
    '''
    # Value to keep track of the string index in the key.
    key_index = 0
    # Get the ascii value of the 'a' char.
    a_value = ord('a')
    # Store decryption result in this variable.
    decrypted_message = ""

    for letter in message:
        if(letter != " "):
            # Shift the letter to the apropriate alphabet index. EX: a = 0, b = 1, c = 2, also get the ASCII value of the letter.
            letter_value = ord(letter) - a_value
            # Get the ascii value of the key letter.
            key_value = ord(key[key_index]) - a_value
            # Properly shift the letter down by the key at index i and typecast back to a character.
            new_letter_value = (letter_value - key_value)

            # If the numbers are shifted backwards past 0 (negative) then offset by 26. (Numbers should go backwards starting from 26.)
            if(new_letter_value < 0):
                new_letter_value += 26

            # Increase the index of the key.
            key_index = (key_index + 1) % len(key)
            # Store the newly shifted letter.
            letter = chr(new_letter_value + a_value)

        # Store letter in decrypted_message string variable.
        decrypted_message += letter

    return decrypted_message

def wordsInDictionary(wordList, dictionary):
    '''
    Checks if all the words are in the dictionary.
    '''
    result = True

    for word in wordList:
        # Append a new line to the word so that it can properly match in the dictionary.txt file.
        word += "\n"
        # Check if the word is not in the dictionary.
        if word not in dictionary:
            # If it is not then set the result to false.
            result = False
    return result

def crackMessage():
    dictionary = open("dictionary.txt", "r")
    result_file = open("results.txt", "w")
    for word in dictionary:
        result_file.write(decryptVignere(CIPHER_TEXT, word.strip("\n")) + "\n")


if __name__ == "__main__":
    crackMessage()

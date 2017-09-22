"""
OSS Challenge #2 - Vignere Cipher [Brute Force] Solution
Anthony Nguyen
9/21/17

Explanation
------------
What we know:
 - Vignere Cipher.
 - Key is a 4 letter word.
 - Key is a word in the dictionary.
 - All plain text words are in the dictionary.

Pseudo-Code
-----------
open dictionary file.

for each four letter word in the dictionary
  Attempt to decrypt the cipher text with the four letter word.
    If the results of the decryption are words from the dictionary
        Store the key in a text and write the plain text to results.txt.
"""

CIPHER_TEXT = "vp fulp go xcvne jbul ziafevny"

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

def wordInDictionary(word):
    '''
    Checks if all the words are in the dictionary.
    '''
    dictionary = open("dictionary.txt", "r")
    word_found = False

    # If the word is in the dictionary then set result to True.
    if (word + "\n") in dictionary:
        word_found = True
    dictionary.close()

    return word_found

def crackMessage():
    dictionary = open("dictionary.txt", "r")
    result_file = open("results.txt", "w")
    for word in dictionary:
        print("Decrypting with key: " + word)
        decrypted_message = decryptVignere(CIPHER_TEXT, word.strip("\n"))
        message_word = decrypted_message.split()[5]

        # If all words in the list are in the dictionary write it to results.txt
        if wordInDictionary(word_list):
            result_file.write("Plain Text: ")
            result_file.write(decrypted_message + "\n")
            result_file.write("Key: ")
            result_file.write(word)

if __name__ == "__main__":
    crackMessage()

    print("Finished, results stored in results.txt.")

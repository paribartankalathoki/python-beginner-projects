
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Function to encode the message
def encodeMessage(message):

    encryptedWords = []

    for msg in message.split(" "):

        if len(msg) < 3:
            encryptedWords.append(msg[::-1])

        else:
            randomChar1 = ""
            randomChar2 = ""

            for _ in range(3):
                randomChar1 += random.choice(characters)

            for _ in range(3):
                randomChar2 += random.choice(characters)

            encryptedWords.append(randomChar1 + msg[1:] + msg[0] + randomChar2)

    return " ".join(encryptedWords)


# Function to decode the message
def decodeMessage(message):

    decryptedWords = []

    for msg in message.split(" "):

        if len(msg) < 3:
            decryptedWords.append(msg[::-1])

        else:
            actualWord = msg[3:-3]
            originalWord = actualWord[-1] + actualWord[:-1]

            decryptedWords.append(originalWord)

    return " ".join(decryptedWords)


# Main program
print("\nWelcome to Secret Code Language!")

while True:

    print("\nWhat do you want to do?")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        message = input("\nEnter message to encode: ")

        result = encodeMessage(message)

        print("\nEncoded Message:", result)

    elif choice == "2":
        message = input("\nEnter message to decode: ")

        result = decodeMessage(message)

        print("\nDecoded Message:", result)

    elif choice == "3":
        print("\nThank you for using Secret Code Language!")
        break

    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")

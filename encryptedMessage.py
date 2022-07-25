import string


def encrypt_message(msg, rot=13):
    encoded_message = []
    for letter in msg:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            encoded_letter_index = (letter_index + rot) % 26
            encoded_letter = alphabet[encoded_letter_index]
            encoded_message.append(encoded_letter)
        else:
            encoded_message.append(letter)
    encoded_message = "".join(encoded_message)
    return encoded_message


def encrypt_with_key(msg, key):
    encrypted_message = []
    counter = 0
    for letter in msg:
        key_letter = key[counter % len(key)]
        key_index = alphabet.index(key_letter)
        encrypted_letter = encrypt_message(letter, key_index)
        counter += 1
        encrypted_message.append(encrypted_letter)
    return "".join(encrypted_message)


if __name__ == "__main__":
    alphabet = list(string.ascii_lowercase)
    key = "mehdi"
    print("hello, I'm an encryption program!")
    result = input("what is your secret? ")
    secret = encrypt_with_key(result, key)
    print("your secret message is: {}".format(secret))

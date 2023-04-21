def caesar_cipher(message, key, mode):
    """Encrypt or decrypt a message using the Caesar cipher."""
    # Determine whether to encrypt or decrypt
    if mode == 'e':
        shift = key
    elif mode == 'd':
        shift = -key
    else:
        raise ValueError("Invalid mode. Use 'e' for encryption or 'd' for decryption.")

    # Convert message to uppercase
    message = message.upper()

    # Initialize empty result string
    result = ''

    # Loop over each character in the message
    for char in message:
        # Only encrypt/decrypt alphabetical characters
        if char.isalpha():
            # Shift the character by the key
            new_char_code = ord(char) + shift
            # Wrap around to beginning of alphabet if necessary
            if new_char_code > ord('Z'):
                new_char_code -= 26
            elif new_char_code < ord('A'):
                new_char_code += 26
            # Convert the new character code back to a character and append to result
            result += chr(new_char_code)
        else:
            # Append non-alphabetical characters unchanged
            result += char

    return result

# Get user input for mode, key, and message
mode = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")
key = int(input("Please enter the key (0 to 25) to use.\n> "))
message = input("Enter the message to {}.\n> ".format('encrypt' if mode == 'e' else 'decrypt'))

# Encrypt or decrypt the message using the Caesar cipher
result = caesar_cipher(message, key, mode)

# Print the result
print(result)
"""
Output: Example
Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 3
Enter the message to encrypt.
> ABC
DEF

Process finished with exit code 0
"""

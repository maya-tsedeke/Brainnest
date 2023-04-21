## Caesar Cipher (advanced)
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar to encrypt messages. It encrypts letters by shifting them over by a certain number of places in the alphabet. The length of the shift is called the key. For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction.

This program lets the user encrypt and decrypt messages according to this algorithm. It prompts the user for the mode (encryption or decryption), the key, and the message to be encrypted or decrypted
### Function description
The function caesar_cipher() takes a message string, a key integer, and a mode string ('e' for encryption or 'd' for decryption) as input. It returns the encrypted or decrypted message as a string.

The function first determines whether to encrypt or decrypt based on the mode input. If mode is 'e', it sets the shift to the key value. If mode is 'd', it sets the shift to the negative of the key value. If mode is neither 'e' nor 'd', the function raises a ValueError.

The function then converts the message to uppercase, since the Caesar cipher is case-insensitive. It initializes an empty result string and loops over each character in the message. It only encrypts or decrypts alphabetical characters, leaving non-alphabetical characters unchanged. It shifts each alphabetical character by the key value, wrapping around to the beginning of the alphabet if necessary. Finally, it converts each new character code back to a character and appends it to the result string.

In the main program, the user is prompted for the mode, key, and message inputs using the input() function. The format() method is used to insert the word "encrypt" or "decrypt" into the prompt string depending on the mode input. The caesar_cipher() function is then called with these inputs, and the result is printed.
### Installation
To use this program, simply clone the GitHub repository and run the caesar_cipher.py file in your Python environment. This program requires Python 3 or higher to run.

### Usage
To use the Caesar cipher program, run the caesar_cipher.py file in your Python environment. You will be prompted to enter the mode (encryption or decryption), the key (a number from 0 to 25), and the message to be encrypted or decrypted.

### Example usage:
```` 
   Do you want to (e)ncrypt or (d)ecrypt?
   > e
   Please enter the key (0 to 25) to use.
   > 4
   Enter the message to encrypt.
   > Meet me by the rose bushes tonight.
   QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
   
   Do you want to (e)ncrypt or (d)ecrypt?
   > d
   Please enter the key (0 to 25) to use.
   > 4
   Enter the message to decrypt.
   > QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
   MEET ME BY THE ROSE BUSHES TONIGHT.
````

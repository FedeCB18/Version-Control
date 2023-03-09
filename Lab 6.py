# Import used for array function
import numpy as np

# Convert number string into malleable array
# Encode Array
# Convert array back into number string
def encode(num):
    lis = [int(x) for x in str(num)]
    arr = np.array(lis)
    val = arr+3
    res = ''.join(map(str, val))
    return res

# Convert number string into malleable array
# Decode Array
def decode(password:list):
    decode = ''
    for i in password:
        if int(i) < 3:
            i = (10 + int(i)) - 3
        else:
            i = int(i) - 3
        decode += str(i)
    return decode

# Main Code
if __name__ == "__main__":
    # Loop Function to keep program active unless option 3 is called.
    while True:
        # Menu Options & Input Value for Menu Options
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        inpt = int(input('\nPlease enter an option: '))

        # Backend Menu Structure
        if inpt == 1:
            # Input Value for password
            # Encode Funtion
            # Print Output Statement
            numb = int(input('Please enter your password to encode: '))
            num = encode(numb)
            print('You password has been encoded and stored!')
        elif inpt == 2:
            # Try & Except function used in case option 2 is called before option 1
            # Print Output statement
            try: 
                 print("The encoded password is", encode(numb), end=',')
                 print(' and the original password is', str(numb), end='.\n\n')
            except:
                 print("Please encode a password first before decoding.")
        elif inpt == 3:
            # End Program
            exit()

import numpy as np


def encode(num):
    lis = [int(x) for x in str(num)]
    arr = np.array(lis)
    val = arr+3
    res = ''.join(map(str, val))
    return res

def decode(password:list):
    decode = ''
    for i in password:
        if int(i) < 3:
            i = (10 + int(i)) - 3
        else:
            i = int(i) - 3
        decode += str(i)
    return decode

if __name__ == "__main__":
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        inpt = int(input('\nPlease enter an option: '))

        if inpt == 1:
            numb = int(input('Please enter your password to encode: '))
            num = encode(numb)
            print('You password has been encoded and stored!')
        elif inpt == 2:
            try: 
                 print("The encoded password is", encode(numb), end=',')
                 print(' and the original password is', str(numb), end='.\n\n')
            except:
                 print("Please encode a password first before decoding.")
        elif inpt == 3:
            exit()
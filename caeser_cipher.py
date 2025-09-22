def main():
    alpha_list = [
    'a','b','c','d','e','f','g','h',
    'i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x',
    'y','z'
    ]
    
    while True:
        option = int(input("1. Encode a String to Caeser Cipher\n2. Decode Caeser Cipher to a String\n3. Exit\n"))
        if option == 1:
            encode = caeser_cipher_encode(alpha_list)
            print(f"Encoded String is {encode}")
        elif option == 2:
            decode = caeser_cipher_decode(alpha_list)
            print(f"Decoded String is {decode}")
        elif option == 3:
            print("Exiting the program !")
            break
        else:
            print("Wrong option")
    
def caeser_cipher_encode(alpha_list):
    shift = int(input("Enter the Shift Value\n"))
    message = input("Enter the message\n").lower()
    encode = ''
    for letter in message:
        for index, value in enumerate(alpha_list):
            if letter in value:
                shift_value = (index+shift)%len(alpha_list)
                encode += alpha_list[shift_value]
    return encode

def caeser_cipher_decode(alpha_list):
    shift = int(input("Enter the number\n"))
    message = input("Enter the Shift Value\n").lower()
    decode = ''
    for letter in message:
        for index, value in enumerate(alpha_list):
            if letter in value:
                shift_value = (index-shift) % len(alpha_list)
                decode += alpha_list[shift_value]
    return decode

main()

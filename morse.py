def main():
    alphanum_morse = {
        '1':'.----','2':'..---','3':'...--','4':'....-',
        '5':'.....','6':'-....','7':'--...',
        '8':'---..','9':'----.','0':'-----',
        " ":" ",
        'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',
        'f':'..-.','g':'--.','h':'....','i':'..',
        'j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.',
        'o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...',
        't':'-','u':'..-','v':'...-','w':'.--',
        'x':'-..-','y':'-.--','z':'--..'}
    
    while True :
        option = int(input("""1. Encode a String to Morse code\n2. Decode Morse to a String\n3. Exit\n"""))
        if option == 1:
            alph = input("Enter a String: \n").lower()
            alph_to_morse = from_alphanum_to_morse(alph,alphanum_morse)
            print(alph_to_morse)
        elif option == 2:
            morse = input('Enter morse code: \n')
            morse_to_alph = from_morse_to_alphanum(morse,alphanum_morse)
            print(morse_to_alph)
        elif option == 3:
            break
        else:
            print(f"{option} is an invaild option")
   

def from_alphanum_to_morse(strings,alphanum_morse):
    morse_string = ''
    for string in strings:
        morse_string += alphanum_morse[string]
        morse_string += ' '
    return morse_string

def from_morse_to_alphanum(morse_str,alphanum_morse):    
    decoded_str = ''
    morse_string = ''
    morse_str += ' '

    for string in morse_str:
        if string != ' ':
            morse_string += string
        else:
            for alphanum, morse in alphanum_morse.items():                
                if (morse_string == morse):
                    decoded_str += alphanum
            morse_string = ''
    return decoded_str

main()

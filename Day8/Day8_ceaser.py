alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def ceaser(direction,text,shift):
                encrypt_text=''
                if direction == 'decode':
                        shift*=-1
                for letter in text:
                    if letter not in alphabet:
                           encrypt_text+=letter
                    else:
                        index=alphabet.index(letter)
                        encrypt_text+=alphabet[index+shift]
                print(encrypt_text)  
                
ceaser(direction,text,shift)                  
restart=input('Do you want to go again?')

if restart=='yes':
        ceaser(direction,text,shift)        

          


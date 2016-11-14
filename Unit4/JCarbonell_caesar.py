def get_cipher_letter(new_key,letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alpha:
        return alpha[new_key]
    else:
        return letter




def encrypt(key,message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for letter in message:
        new_key = (alpha.find(letter) + key) % len(alpha)
        result = result + get_cipher_letter(new_key,letter)

    return result



def decrypt(key,message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for letter in message:
        new_key = (alpha.find(letter) - key) % len(alpha)
        result = result + get_cipher_letter(new_key,letter)
        

    return result



def main():
    word = "Hello World?!"

    encrypted = encrypt(20,word)
    print(encrypted)

    
    decrypted = decrypt(20,encrypted)
    print(decrypted) 

if __name__ == "__main__":
    main()
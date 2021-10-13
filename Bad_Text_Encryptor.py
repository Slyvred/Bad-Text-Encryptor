import os

alpha = " ',.;:/\!?@(){}[]°\"=+-_*%0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzàéêëôîùç" #
def encrypt(text, key):
    for i in range(len(text)):
        cipher_text = ""
        for letter in text:
            if (alpha.find(letter) + key) >= len(alpha):
                cipher_text += alpha[(alpha.find(letter) + key) - len(alpha)]
            else:
                cipher_text += alpha[alpha.find(letter) + key]
        text = cipher_text

    return cipher_text

def decrypt(text, key):
    for i in range(len(text)):
        plain_text = ""
        for letter in text:
            if (alpha.find(letter) - key) >= len(alpha):
                plain_text += alpha[(alpha.find(letter) - key) - len(alpha)]
            elif (alpha.find(letter) - key) < 0:
                plain_text += alpha[(alpha.find(letter) - key) + len(alpha)]
            else:
                plain_text += alpha[alpha.find(letter) - key]
        text = plain_text
    return plain_text


def main():
    input_msg = input("Enter some text: ")
    choice = int(input("\n(1) Encrypt\n(2) Decrypt\nChoose an option (1/2): "))
    output = ""
    key = len(input_msg) % len(alpha)
    
    if choice == 1:
        output = encrypt(input_msg, key)
    elif choice == 2:
        output = decrypt(input_msg, key)
    
    print(f"\nThe processed text is: \"{output}\"\n")
    os.system('pause')

if __name__ == "__main__":
    main()

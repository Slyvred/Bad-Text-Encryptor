input_msg = input("Enter some text: ")

choice = int(input("\n(1) Encrypt\n(2) Decrypt\nChoose an option: "))
alpha = " ',.;:/\!?@(){}[]°\"=+-*%0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
key = len(input_msg) % len(alpha)
output_msg = ""

for i in range(len(input_msg)):
    output_msg = ""
    for letter in input_msg:
        if choice == 1:
            if (alpha.find(letter) + key) >= len(alpha):
                output_msg += alpha[(alpha.find(letter) + key) - len(alpha)]
            else:
                output_msg += alpha[alpha.find(letter) + key]
        elif choice == 2:
            if (alpha.find(letter) - key) >= len(alpha):
                output_msg += alpha[(alpha.find(letter) - key) - len(alpha)]
            elif (alpha.find(letter) - key) < 0:
                output_msg += alpha[(alpha.find(letter) - key) + len(alpha)]
            else:
                output_msg += alpha[alpha.find(letter) - key]
    input_msg = output_msg

print(f"\nThe processed text is: \"{output_msg}\"\n")
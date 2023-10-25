#COP3502 Fall 2023
#Corey Cavalli
#Lab 6


# Implemented by Andres De la Flor
# Decodes the encoded password
def decode(password):
    original = ""

    # Loop through the encoded password to revert each character to its original
    for digit in password:
        shifted = (int(digit) + 10 - 3) % 10
        # Add 10 so we can shift each number back by 3, and the ones digit is our decoded digit
        original += str(shifted)

    return original

if __name__ == '__main__':

    en_password = ''
    option = 0
    while(option != 3): #Prompt user with menu until they select quit (option 3)
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: ")) #get user selection

        if(option == 1): #encode
            en_password = '' #new string that holds the encoded password
            password = input("Please enter your password to encode: ")

            for index in range(len(password)): #perform the encryption by shifting each number by 3
                if(password[index] == '0'): en_password += '3'
                elif(password[index] == '1'): en_password += '4'
                elif(password[index] == '2'): en_password += '5'
                elif(password[index] == '3'): en_password += '6'
                elif(password[index] == '4'): en_password += '7'
                elif(password[index] == '5'): en_password += '8'
                elif(password[index] == '6'): en_password += '9'
                elif(password[index] == '7'): en_password += '0'
                elif(password[index] == '8'): en_password += '1'
                elif(password[index] == '9'): en_password += '2'

            print("Your password has been encoded and stored!\n")


        elif(option == 2): #decode
            print(f"The encoded password is {en_password}, and the original password is {decode(en_password)}.")

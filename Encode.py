# Evangeline Decode
def decoder(new_password)
    password_decoded = ""
        for digit_ in new_password:
            old_digit = int(digit_) - 3
            if old_digit < 0:
                old_digit = 9
            password_decoded = password_decoded + str(old_digit)
    return password_decoded

# Starting Renan Enconde/Decode
option =1
while option != 3:
    option = int(input(f"Menu\n"
                       "-------------\n"
                       "1. Encode\n"
                       "2. Decode \n"
                       "3. Quit \n"
                       "\n" # Spacing for Menu
                       "Please enter an option: "))
    if option == 1:
        password = (input("Please enter your password to encode: "))
        new_password = ""
        for digit in password:
            new_digit = str((int(digit) + 3) % 10)
            new_password += new_digit
        password_encoded = new_password
        print(f"Your password has been encoded and stored !"
                "\n") # Spacing for Menu

    if option == 2:
        # Evangeline Decode
        password_decoded = decoder(new_password)
        
        print(f"The encoded password is {password_encoded}, and the original password is {password_decoded}."
               "\n") # Spacing for Menu


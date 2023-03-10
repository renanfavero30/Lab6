

# Starting Renan Enconde/Decode
option =1
while option != 3:
    option = int(input(f"Menu\n"
                       "-------------\n"
                       "1. Encode\n"
                       "2. Decode \n"
                       "3. Quit \n"
                       "Please enter an option: "))
    if option == 1:
        password = (input("Please enter your password to encode: "))
        new_password = ""
        for digit in password:
            new_digit = str((int(digit) + 3) % 10)
            new_password += new_digit
        password_encoded = new_password
        print(f"Your password has been encoded and stored !")


    if option == 2:
        pass

        print(f"The encoded password is {password_encoded}, and the original password is {password_decode}.")



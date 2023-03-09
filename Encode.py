
key = 33333333
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
        password = int(input("Please enter your password to encode: "))
        password_encoded = password + key
        print("Your password has been encoded and stored!")

    if option == 2:
        password_decode = password_encoded - key
        print(f"The encoded password is {password_encoded}, and the original password is {password_decode}.")


#t3st
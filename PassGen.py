import string
import random
import time as t
import os
import colorama
from colorama import  Fore,Style
G = Fore.GREEN
B = Fore.BLUE
R = Fore.RED
C = Fore.CYAN
G = Fore.GREEN
M = Fore.MAGENTA
W = Fore.WHITE
Y = Fore.YELLOW
try:
        import colorama
except ModuleNotFoundError:
        print("Requests is not Installed")
        os.system("pip install colorama")
x= "Enter a valid option!"
os.system ("clear")
print(Fore.BLUE+"""βπΈππ-πΎπΌβ ππ€ π π‘πͺπ₯ππ π π₯π π π ππ π£ πππππ£ππ₯πππ π€π₯π£π ππ π‘ππ€π€π¨π π£ππ€
""")
t.sleep(4)
os.system("clear")
print(Fore.GREEN+"=====================================================")
def loop():
    os.system("clear")
    print(Fore.BLUE+"""
        [+]Tool Name:PASS-GEN
        [+]Creator:LΓͺkzΓ―
        [+]Contact me on whatsapp:+2347064822519
        """)
    print(Fore.GREEN+"=====================================================")
    t.sleep(2)
## characters to generate password from
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#$%^&*()")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    def generate_random_password():
        ## length of password from the user
            length = int(input("Enter password length: "))

        ## number of character types
            alphabets_count = int(input("Enter alphabets count in password: "))
            digits_count = int(input("Enter digits count in password: "))
            special_characters_count = int(input("Enter special characters count in password: "))

            characters_count = alphabets_count + digits_count + special_characters_count

        ## check the total length with characters sum count
        ## print not valid if the sum is greater than length
            if characters_count > length:
                    print(Fore.RED + "Characters total count is greater than the password length" + Style.RESET_ALL)
                    return


        ## initializing the password
            password = []

        ## picking random alphabets
            for i in range(alphabets_count):
                    password.append(random.choice(alphabets))


        ## picking random digits
            for i in range(digits_count):
                    password.append(random.choice(digits))


        ## picking random alphabets
            for i in range(special_characters_count):
                password.append(random.choice(special_characters))


        ## if the total characters count is less than the password length
        ## add random characters to make it equal to the length
            if characters_count < length:
                    random.shuffle(characters)
                    for i in range(length - characters_count):
                           password.append(random.choice(characters))


        ## shuffling the resultant password
            random.shuffle(password)

        ## converting the list to string
        ## printing the list
            print(Fore.BLUE + "Generating password...")
            t.sleep(3)
            print("".join(password))



## invoking the function
    generate_random_password()
    cont = input(Fore.GREEN + "Do you wanna continue? [y/n]: ")
    if cont == "y" or cont == "Y":
           loop()
loop()
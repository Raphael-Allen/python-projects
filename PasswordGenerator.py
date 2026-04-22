import random
import string

class RandomPassword:
    def __init__(self):
        self.password = []
        self.upper = string.ascii_uppercase
        self.lower = string.ascii_lowercase
        self.digits = string.digits
        self.special = string.punctuation
    
    def get_character_pool(self):
        self.pool = ""
        get_upper = input("Do you want upper case characters in your password? 1.Yes 2.No ")
        if get_upper == "1":
            self.pool += string.ascii_uppercase
        elif get_upper == "2":
            pass

        get_lower = input("Do you want lower case characters in your password? 1.Yes 2.No ")
        if get_lower == "1":
            self.pool += string.ascii_lowercase
        elif get_lower == "2":
            pass

        get_digits = input("Do you want digits in your password? 1.Yes 2.No ")
        if get_digits == "1":
            self.pool += string.digits
        elif get_digits == "2":
            pass

        get_special = input("Do you want special characters in your password? 1.Yes 2.No ")
        if get_special == "1":
            self.pool += string.punctuation
        elif get_special == "2":
            pass
        if self.pool == "":
            print("Error: You must select at least one type of character ") 
            return  
    
    def password_generator(self):
        self.password = []
        self.characters = int(input("How many characters do you want in your password? "))
        for i in range(self.characters):
            self.password.append(random.choice(self.pool))
        print(f"Your password is {''.join(self.password)}")

    def run(self):
        while True:
            select = input("1. Create Password 2. Quit ")
            if select == "1":
                self.get_character_pool()
                if self.pool != "":
                    self.password_generator()
            elif select == "2":
                return
            else: print("Error: Input not recognized ")  

ranpass = RandomPassword()
ranpass.run()


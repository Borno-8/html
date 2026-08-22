class iosstring():

    def __init__(self):
        self.str1 = ""

    def get_s(self):
        self.str1 = input("Enter String : ")

    def print_s(self):
        print("Result is :", self.str1.upper())

str1 = iosstring()

str1.get_s()
str1.print_s()
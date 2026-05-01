import sys

def initial_phonebook():

    rows, cols= int(input("Please enter initial number of congrats")), 5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" %
(i+1))
        
        print("NOTE: * indicates mandatory feilds")

        print(".............................................")
        temp = []
        for j in range(cols)


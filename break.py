a = input ("Enta a word: ")

for i in a:
    if (i == 'A' or i == 'a'):
        print("@ is found")
        break
    else:
        print("@ is not found, sorry :(")
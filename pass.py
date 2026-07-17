for x in range (11):
    if x % 20 == 0:
        print("twist")
    
    elif x % 15 == 0:
        pass

    elif x % 5 == 0:
        print("Fizz")

    elif x % 3 == 0:
        print(x)
        print("buzz")

    else:
        print(x)
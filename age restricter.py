try:
    number = int(input("Enta ur num"))
    print("da number entad is", number)
except ValueError as ex:
    print("Exception:", ex)
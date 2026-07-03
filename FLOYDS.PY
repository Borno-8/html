rows = int(input("Please Enter da total Num of roows :"))
number = 1

print("Floyd's tri anguul")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end = ' ')
        number = number + 1
    print()
string = input("Please enter ur own word : ")
char = input("Please enter ur own something")
i = 0
count = 0
while(i < len(string)):

    if(string[i] == char):
        count = count + 1
    i = i + 1

print("the tatal numba of of times ", char, "has APEARED = ", count)
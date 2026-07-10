def  add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

print ("Please select the math thing")
print ("a. Add")
print ("b. minus")
print ("c. times")
print ("d. divide")

choice = input("Please enter only one letter")

num_1 = int(input("Please enter da first num: "))
num_2 = int(input("Please enter da second num: "))

if choice == 'a':
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
   print (num_1, " - ", num_2, " = ", sub(num_1, num_2))

elif choice == 'c':
   print (num_1, " x ", num_2, " = ", mul(num_1, num_2))

elif choice == 'd':
   print (num_1, " ÷ ", num_2, " = ", div(num_1, num_2))
else:
    print("u r dumb wrong things typed in")
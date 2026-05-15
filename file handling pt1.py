with open('C:/Python/codingal.text', 'w') as file:
    file.write("hi im penguim, im 1 years old")
    file.close()
with open ('C:/Python/codingal.text','r') as file:
    data = file.readlines()
    print("words in this file are....")
    for line in data:
     word = line.split()
    print (word)
    file.close

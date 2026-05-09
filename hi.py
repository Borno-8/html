file = open('C:/Python/codingal.text','r')
print(file.read())
file.close()

file = open('C:/Python/codingal.text')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('C:/Python/codingal.text', 'a')
file.write(" Hi! I am dum.")
file.close()
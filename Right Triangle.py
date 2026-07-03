print("Half Pyramid Pattern of Stars! (🌟):")
n = int(input("enter da numba of rows"))
for i in range(n):
    for j in range(i+1):
        print("🌟 ", end="")
    print()
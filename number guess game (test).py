secret_num = 27
life_count = 5

print("WELCOME tooooooo DA NUMBA GUESSING GAME🚀")
print("Guess the secrat numba between 1 & 50!")
print("U have 5 lives. \n")

while life_count > 0:
    guess = int(input("Enta ur guess!"))

    if guess == secret_num:
        print("CONGRATULATIONS, u found da numba")

    difference = abs(secret_num - guess)

    if difference > 20:
        print("bro u dumb, ur ice")
        print("bro u dumb, ur ice")
def no_notes(a):
    Q = [1000, 500, 100, 50, 10, 5, 1]
    X = 0
    for i in range(7):
        q = Q[i]
        X = a//q
        print("Notes of {} = {}".format(q, X))
        a = a%q

amount = int(input("Enter total amount"))
no_notes(amount)
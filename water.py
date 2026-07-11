def c(amount,tip_perc):
    total = amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"PAY ${total} RIGHT NOW!!!")

c(150,20)
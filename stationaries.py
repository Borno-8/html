items = ["pencil", "earaser", "sharpner", "glue"]
s_c = [12, 0, 8, 5, 3]

inv = {i: count for i, count in zip(items, s_c)}
print("Full Inventory:", inv)

i_s_t = [i for i in items if inv[i] > 0]
print("Items in stock:", i_s_t)

c_i = input("Which Item do u want to buy? ")
if c_i not in inv or inv[c_i] == 0:
    print(c_i, "is out of stock! soo STOP CHECKING")
    exit()

prices = [10, 5, 40, 15, 20]
markup = int(input("enter the makup amont to add to add to every price: "))

marked_up_prices = list(map(lambda p: p + markup, prices ))
print("marked up prices:", marked_up_prices)

item_index = items.index(c_i)
chosen_prices = marked_up_prices[item_index]
print("Price of", c_i, "after markup:", chosen_prices)

inv[c_i] = inv[c_i] - 1
print(c_i, "PURCHASED! stock left", inv[c_i])

print("")
print("===== SCHOOL STORE INVENTORY CHECKER =====")
print("Item Bought:", c_i)
print("Price Paid:", chosen_prices)
print("Update Inventory:", inv)
print("==========================================")
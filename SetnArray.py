basket1 = {"apple", "nana", "Mangos", "apple", "graaaaaaapes"}
basket2 = {"mango", "KIWII", "nana", "KIWII"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("Orangutan")
print("Basket 1 after adding the ape:", basket1)

common_f = basket1.intersection(basket2)
print("Fruits in both baskets:", common_f)

import array as arr
fruit_c = arr.array('i', [3, 5, 2, 4])
print("Fruit counts array", fruit_c)

fruit_c.insert(0, 1)
fruit_c.append(6)
print("Fruit counts after adding items:", fruit_c)

count_of_4 = fruit_c.count(4)
print("Numbers of times 4 appers:", count_of_4)

fruit_c.reverse()
print("Reversed fruit counts array:", fruit_c)
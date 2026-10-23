import numpy as np
data_type = [('fruit', 'S10'), ('quantity', int), ('price', float)]
fruit_details = [('Apple', 10, 30.5), ('Mango', 5, 45.0), ('Banana', 12, 15.75)]
fruits = np.array(fruit_details, dtype=data_type)
print(fruits)


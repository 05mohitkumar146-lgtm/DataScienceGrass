# ques
# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
import numpy as np 
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

#Print the complete dataset
print(sales_data)
# Find the shape of the array.
print(sales_data.shape)
# Find the number of dimensions.
print(sales_data.ndim)
# Find the total number of elements.
print("total number of elements",sales_data.size)
# Print only Restaurant IDs.
print("IDs")
for i in range(len(sales_data)):
    print(sales_data[i][0],end=" ")
# Print 2021 sales data.
print("\n 2021 sales data")
for i in range(len(sales_data)):
    print(sales_data[i][1],end=" ")
# Print 2024 sales data
print("\n 2024 sales data")
for i in range(len(sales_data)):
    print(sales_data[i][-1],end=" ")
# Find the maximum sales value
print("max sales value",sales_data.max())
# Find the minimum sales value.
print("min sales value",sales_data.min())
# Find total sales of all restaurants in 2021.

sum=0
for i in range(len(sales_data)): 
    sum+=sales_data[i][1] 
print("total sales of all restaurants in 2021.",sum)
# Find average sales in 2024.
avg=0
for i in range(len(sales_data)): 
    avg+=sales_data[i][-1] 
print("average sales in 2024.",(avg/len(sales_data)))
# Find total sales of each restaurant.

for i in range(len(sales_data)): 
    total=0
    for j in range(1,len(sales_data[i])): 
        total+=sales_data[i][j]
    print(f"total sales of {i} restaurant is {total}")
# Find average sales of each restaurant.
for i in range(len(sales_data)): 
    avg=0
    for j in range(1,len(sales_data[i])): 
        avg+=sales_data[i][j]
    print(f"average sales of {i} restaurant is {avg/len(sales_data)}")
import numpy as np

print("\nString Indexing Array:- You can access the indivuale charectes in a string their index.")
# syntax:
#   string[index_value]

x = "DINES"
print(x)
# Access the index posion
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print()

index_value = np.array([1,2,3,4])
print("Array :",index_value)

# Access the array posion
print("Index 0:", index_value[0])
print("Index 1:", index_value[1])
print("Index 2:", index_value[2])
print("Index 3:", index_value[3])
print()

negative_index = np.array([1,2,3,"D","K",4])
print("Array :", negative_index)

# 1. Nagative Indexing Array <-------used to access elements of an array form its end.
print("Index -1:",negative_index[-1])
print("Index -2:",negative_index[-2])
print("Index -3:",negative_index[-3])
print("Index -4:",negative_index[-4])
print("Index -5:",negative_index[-5])
print("Index -6:",negative_index[-6])
print()

negative_index = np.array([1, "DOG", 2, "CAT", 3, "D", "K", "RAT", 5, True])
print("Array :",negative_index)

# 2. Nagative Indexing Array
print("Index -1:",negative_index[-1])
print("Index -2:",negative_index[-2])
print("Index -3:",negative_index[-3])
print("Index -4:",negative_index[-4])
print("Index -5:",negative_index[-5])
print("Index -6:",negative_index[-6])
print("Index -7:",negative_index[-7])
print("Index -8:",negative_index[-8])
print("Index -9:",negative_index[-9])
print("Index -10:",negative_index[-10])


import numpy as np

# 2D Array
ar = np.array([[2, 3 , 4], [5, 6, 7]])

print("2D Array:",ar)
print()

# Access to 2D array
print("frist row:", ar[0]) # Output : frist row 
print("Second row:", ar[1]) # Output : Second row
print()
print(ar[0][0]) # Output : 2
print(ar[0][1]) # Output : 3
print(ar[0][2]) # Output : 4
print()
print(ar[1][0]) # Output :3
print(ar[1][1]) # Output :5
print(ar[1][2]) # Output :5

# Slicing used 2d array
print()
print(ar[1:,0]) # Output :5
print(ar[1:,1]) # Output :6
print(ar[1:,2]) # Output :7
print()
print(ar[0:,0]) # Output :[2 5]
print(ar[0:,1]) # Output :[3 6]
print(ar[0:,2]) # Output :[4 7]

print()
# 2D Array Type 2
array = np.array([[2, 3 , 4], [5, 6, 7], [8, 9, 10]])

print(array) # 2D Array
print("Type array Dimentional:",array.ndim)

# Access to 2D array
print("\nfrist row:", array[0]) # Output : frist row 
print("\nSecond row:", array[1]) # Output : Second row
print("\nThird row:", array[2]) # Output : Second row
print()
print(array[0][2]) # 1ST row 3rd colum
print(array[1][2]) # 2ST row 3rd colum
print(array[2][2]) # 3rd row 3rd colum

# Slicing used 2d array
print(array[0:,0])
print(array[0:,1])
print(array[0:,2])

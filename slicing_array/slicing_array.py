
import numpy as np

print("\nSlicing Array:-Slicing is used to access elements of an array using a range of two indexes.\n")


slicing_array = np.array([1, "DOG", 2, "CAT", 3, "D", "K", "RAT", 5, True])
print("Array :",slicing_array)
print()
# 1.Access Slicing Array:- Syntax: Variable_Name(startIndex: endIndex-1)
print("Slicing start index 2 to index 5:", slicing_array[2:5]) # ouput : ['2', 'CAT', '3']
print("Slicing start index 0 to index 3:", slicing_array[0:3]) # ouput : [1, DOG, 2]
print("Slicing start index 6 to index 10:", slicing_array[6:10]) # ouput : ['K', 'RAT', '5', 'True']
print()

print("Slicing start from index 4 to end index:", slicing_array[4:]) # ouput : ['3', 'D', 'K', 'RAT', '5', 'True']
print("Slicing start from  index (4-1) to end start index:", slicing_array[:4]) # ouput : ['1', 'DOG', 2, 'CAT',]
print("Slicing start from  index (5-1) to end start index:", slicing_array[:5]) # ouput : ['1', 'DOG', 2, 'CAT','3']
print()


slicing = np.array([2, 3 , 4, 5, 6, 7, 8, 9, 10, 11])
print("Array",slicing)
print()
# 2. Access Nagative Slicing Array:- 
print("End index:",slicing[-1:])                # output: [11]
print("Last index jump plus all:",slicing[:-1]) # output: [ 2  3  4  5  6  7  8  9 10]
print("last se 5 index to jump last index:",slicing[-5:-1]) # output: [ 7  8  9 10]
print("last se 8 index to jump last 4 index :",slicing[-8:-4]) # output: [4 5 6 7]
print()



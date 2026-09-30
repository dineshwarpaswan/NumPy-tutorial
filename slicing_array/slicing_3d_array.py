
import numpy as np

print()
# 3D Array
array = np.array([[[1, 2 , 3], [4, 5, 6], [7, 8, 9]]])

print("3D Array:",array) # 3D Array
print("Type array Dimentional:",array.ndim)
print("layer,Rows and colums:",array.shape) # Output :(layer, totale rows, totale colums) in shape() method
print("\n" + "=" *15 + "\n")

# TYPE 1 Access to slicing 3D array in row
print("\nTYPE 1 Access to slicing 3D array in row")  
print("1st row:", array[:,0]) # Output : frist row
print("\n" + "=" *5 + "\n")

print("Snd row: ", array[:,1]) # Output : Second row
print("\n" + "=" *5 + "\n")

print("3rd row:", array[:,2]) # Output : 3rd row
print("\n" + "=" *15 + "\n")

# Tytpe 2 Access to slicing 3D array in row
print("\nTytpe 2 Access to slicing 3D array in row")
print("1st row:", array[0:,0]) # Output : frist row
print("\n" + "=" *5 + "\n")
print("Snd row: ", array[0:,1]) # Output : 2nd row
print("\n" + "=" *5 + "\n")
print("3rd row:", array[:,2]) # Output : 3rd row
print("\n" + "=" *15 + "\n")

# Tytpe 3 Access to slicing 3D array in Show Shape 2d array
print("\nTytpe 3 Access to slicing 3D array in show Shape 2D Array")
print(array[0, :, :]) # Output : 2d array
print("Array Dimentional:", array.ndim)
print("layer,Rows and colums:",array.shape) # Output :(layer, totale rows, totale colums) in shape() method
print("\n" + "=" *5 + "\n")

print(array[:, 1, :]) # Output : 2d array
print("Array Dimentional:", array.ndim)
print("\n" + "=" *5 + "\n")

print(array[0, :, 1:]) # Output : 2d array
print("Array Dimentional:", array.ndim)
print("\n" + "=" *5 + "\n")

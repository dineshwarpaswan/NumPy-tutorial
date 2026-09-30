print("\nMathematical Operations on Array:-\n")

import numpy as np


# Mathematical Operation on Array
math_array = np.array([10,20,30,40,50])

print("Array:", math_array)
print()

print("increament+10:", math_array+10)
print("dicreament-10:", math_array-10)
print("multiply by*10:", math_array*10)
print("Divition by/10:", math_array/10)
print("Squaring by**2:", math_array**2)

print("\n" + "*" *20)

data = np.array([1,4,9,16,25])
print("Array:",data)
print()

print("Squaring:", np.square(data))
print("Squareroot:", np.sqrt(data))
print("\n" + "=" *20)

print("Trigometric operation on array:-\n")
# Trigometric operation on array

array = np.array([10, 15, 30, 45, 60,90])
print("Array:", array)
print()

print("Sin:", np.sin(array))
print("Cose:", np.cos(array))
print("Tan:", np.tan(array))
print("\n" + "-" *20)

# Mathematical Operation on Multiple Arrays
print("Mathematical Operation on Multiple Arrays\n")
a = np.array([2, 4, 5])
b = np.array([3, 6, 8])

print("Array 1:", a)
print("Array 2:", b)
print()
print("Array 1 + Array 2:", np.add(a, b))
print("Array 1 - Array 2:", np.subtract(a, b))
print("Array 1 * Array 2:", np.multiply(a, b))
print("Array 1 / Array 2:", np.divide(a, b))
print("\n" + "_" *20)

# dot Product on Multiple Arrays :- Sum of product and there corospodeness multyply element
print("dot Product on Multiple Arrays :- Sum of product and there corospodeness multyply element")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print()
print("Array 1:", x)
print("Array 2:", y)
print("Sum of product and there corospodeness multyply element:", np.dot(x, y))# output of dot(): 1*4 + 2*5 +3*6 =32
print("\n" + "_" *20)

# Transpose on Array
print("Transpose on Array:-\n")
tran = np.array([[1,2,3],[4,5,6]])
print(tran)
print()
print(tran.T)






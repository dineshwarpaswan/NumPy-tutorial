import numpy as NumPy

print("2. Numpy Array Attributes:-\n")
# 2. Numpy Array Attributes
at_array = NumPy.array([[1,2,3,], [4,5,6]])

print(at_array)
print("Totale row and colum in Shape:", at_array.shape) # output:(totale row, total culum)
print("Totale element of array in Size:",at_array.size) # totale element in array
print("Dytpe:", at_array.dtype) # data type int 32/64 bit
print("number of Dimentional:", at_array.ndim) # which array type cheack 

print("\n" + "=" *10)
print("3. Zeros Array Method:-\n")
# 3. Zeros Array: zeros((1,3)) Method
zero_array = NumPy.zeros((1,3)) # zeros shape create
print("Row and Colum Zero shape:",zero_array) # Totale row and culum in zero shape

zero_array = NumPy.zeros((2,3)) # zero shape create
print("\nZero shape:",zero_array) # Totale row and culum in zero shape

print("\n" + "=" *10)

print("3. Ones Array: ones((1,3) Method:-\n")
# 3. Ones Array: ones((1,3) Method
ones_array = NumPy.ones((1,3)) # ones shape create
print("Ones shape:",ones_array) #Totale row and culum in Ones shape
print()

# 3.1 Ones shape:
ones_array = NumPy.ones((2,3)) # zero shape create
print("Ones shape:",ones_array) # Totale row and culum in Ones shape
print("\n" + "=" *10)

print("Full Array: full((3,2),5) Method\n")
# 3. Full Array: full((3,2),5) Method
full_array =NumPy.full((3,2),5) # all value same
print("Full Array:", full_array)
print()
full_array =NumPy.full((2,3),7) # all value same
print("Full Array:", full_array) # Full Array in all value same
print("\n" + "=" *10)

print("4. Identity Matrix: eye(3) Method:-\n")
# 4. Identity Matrix: eye(3) Method
identy_array =NumPy.eye(3)  # all element in dygonal
print("Identity Matrix", identy_array) 
print("\n" + "=" *10)

print("5. Empty Array: empty(2) Method:-\n")
# 5. Empty Array: empty(2) Method
print("Any 2 random values genrate used of Empty, Array ",NumPy.empty(2))  # Argument 2 pass hone per, Any 2 random values genrate
print("\n" + "=" *10)

print("6. Evenly Spaced Array: arange(start,stop,step) Method:-\n")
# 6. Evenly Spaced Array: arange(start,stop,step) Method
print("Evan Array",NumPy.arange(2,9,2))  # 3 Argument(start,stop,step) values genrate: 2,4,6,8
print("Odd Array",NumPy.arange(1,6,2))  # 3 Argument(start,stop,step) values genrate: 1,3,5
print("cequence Array",NumPy.arange(1,5,1))  # take 3 Argument(start,stop,step) values genrate: 1,2,3,4
print("\n" + "=" *30)

print("7. Specific number of equily spaced values between a arange: linspace(3,15,4) Method, take 3 Argument(start, stop, step)genrate: devide same diferecne:-\n")
# 7. Specific number of equily spaced values between a arange: linspace(3,15,4)) method
print("Devide 4 same diferecne linspace Array",NumPy.linspace(3,15,4))  # take 3 Argument(start, stop, step) values genrate: devide 4 same diferecne (3,7,11,15)
print("Devide 3 same diferecne linspace Array",NumPy.linspace(1,10,3))  # take 3 Argument(start, stop, step) values genrate: 
print("Devide 5 same diferecne linspace Array",NumPy.linspace(1,10,5))  # take 3 Argument(start, stop, step) values genrate: devsame diferecne
print("\n" + "*" *10)

print("8.Random Values Array in float: random.rand(3,3) Method, random  values genrate: in float row and colum :-\n")
# 8.Random Values Array in float: random.rand(3,3)) Method
print(NumPy.random.rand(3,3))  # take 2 Argument pass value,random values genrate: in row and colum
print()
print(NumPy.random.rand(2,3))  # take 2 Argument pass values, random values genrate: in row and colum
print("\n" + "=" *15)

print("9. Random Values Array in integer: random.randint(1,10,(3,3)) Medhod, random(sart,end(row value, colum value)) values genrate: in intiger row and colum:-\n")
# 9.Random Values Array in integer: random.randint(1,10,(3,3)) Metodh
print(NumPy.random.randint(1,10,(3,3)))  # take 3 Argument pass values, random values genrate: in row and colum
print()
print(NumPy.random.randint(1,8,(2,3))) # take 3 Argument pass values, random values genrate: in row and colum
print()
print(NumPy.random.randint(1,50,(3,2))) # take 3 Argument pass values, random values genrate: in row and colum







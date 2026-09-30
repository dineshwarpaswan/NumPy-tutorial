print("\nNumPy Arrays:-NumPy arrays are like the better version of python lists. Arrays are much faster than lists,and is easier to work with.\n")

# 1.Create an  Array : use the array()method of NumPy.
import numpy as NumPy

list1 = [45,50,60,70]
print(list1) # <--list seprated cooma me hota hai
print(type(list1))
print()

list2 = [20, 30, 40, 90]
x = NumPy.array(list2) # <--Array list seprated cooma me nahi hota hai
print("single D Array",x)#<-- single Dimenational array
print(type(x))
print("Array Dimenational:",x.ndim) # which array type cheack 

print()
x1 = NumPy.array([1,2,3]) # <-- single Dimenational array
print("single D Array", x1)
print(type(x1))


print()
a = [1,2,3]
b = [4,5,6]

c = NumPy.array([a, b]) #<-- 2 Dimenational array
print("2D Array:",c)
print(type(c))
print("Array Dimenational:",c.ndim) # which array type cheack 

print()
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = NumPy.array([[a, b, c]]) #<-- 3 Dimenational array
print("3D Array:",d)
print(type(d))  
print("Array Dimenational:",d.ndim) # which array cheack 
print()


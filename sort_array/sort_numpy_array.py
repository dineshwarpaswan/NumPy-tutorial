print("\nPyhthon Numpy Sort:-numpy allows us to arrays using the sort() method.")
import numpy as np 

# Shorting From Lowest to Highest Array of number

data = np.array([80,25,60,45,100,95])
print("\nArray:", data)
print("Array Dimentional:", data.ndim,"D Array")

sorting = np.sort(data)
print("Shorting Array From Lowest to Highest Number", sorting)

# Sorting Alphabetically array

str_data = np.array(["Laptop","Mobile","Desktop","Computer"])
print("\nString Array:", str_data)
print("Array Dimentional:", str_data.ndim,"D Array")

str_sort = np.sort(str_data)
print("Shorted Alphabitical Array:", str_sort)

print("\n"+ "=" *15)

print("\n2D and 3D Aarray Sorting:-\n")
# 2D intiger Aarray Sorting:-

numbers = np.array([[20,60,40],[50,10,30]])
print("Array:",numbers)
print("Array Dimentional:", numbers.ndim,"D Array")

Sorted = np.sort((numbers))
print("\nSorted 2D Array:", Sorted)
print("Array Dimentional:", Sorted.ndim,"D Array")

print("\n"+ "*" *10)

# 3D intiger Aarray Sorting:-
numbers1 = np.array([[[20,60,70],[50,10,90],[100,30,80]]])
print("Array:",numbers1)
print("Array Dimentional:", numbers1.ndim,"D Array")

Sorted1 = np.sort((numbers1))
print("\nSorted 3D Array:", Sorted1)
print("Array Dimentional:", Sorted1.ndim,"D Array")
print("\n"+ "=" *15)

#2D String Alphabetically array
print("2D Array Alphabetically:- \n")
String_Array = np.array([['Laptop', 'Mobile', 'Desktop', 'Computer'],['Mause', 'Pendrive','CD',"Kybord"]])

print("String Array 2D:", String_Array)
print("Array Dimentional:", String_Array.ndim, "D Array")

Shorted_Alpha= np.sort((String_Array))
print("\nShorted Alphabitical Array:",Shorted_Alpha) 

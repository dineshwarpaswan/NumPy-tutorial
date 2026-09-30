print("\nPyhthon Numpy Search:- We can search for specific value in array using the where() method.")
import numpy as np 

# Example Search For every  Laptop position:-
print("Example Search For every  Laptop :-\n")

str_data = np.array(["Laptop", "Mobile", "Laptop", "Desktop", "Laptop", "Computer", "Laptop"])

print("String Array:", str_data)
print("Check Dimentional:", str_data.ndim,"D Array")

search_data = np.where(str_data == "Laptop")
print("\nSearched Laptop index posion:", search_data)

print("\n" + "=" *20)

# Find Even and Odd Numbers:-
print("# Find Even and Odd Numbers in Array:-\n")

data_array = np.array([2, 13, 3, 7, 6, 10, 19, 12, 5, 8, 17, 9, 1, 16, 15])
print("\nArray:", data_array)


even_data = np.where(data_array % 2 == 0)

odd_data= np.where(data_array % 2 == 1)

print()
print("Even Numbers")
for even in even_data:
	print(data_array[even])

print()
print("Odd Numbers")
for odd in odd_data:
	print(data_array[odd])


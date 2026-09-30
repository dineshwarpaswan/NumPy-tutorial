
import numpy as np

# Handling with non & inf :
print("\nHandling with nan & inf :-")

data = np.array([1, 2, np.nan, 4, np.inf])
print(data)
print(np.isnan(data))
print(np.nan_to_num(data))

print("\n" + "-" *15)

# Save and load Array
print("Save and load Array:-\n")

array_data = np.array([10, 20, 30, 40])
print("Array:",array_data)

# example 1

# np.save("file.npy", variable_name/object_name)
np.save("my_array.npy", array_data) # my_array name ka file save hojayega,  
laod_array = np.load("my_array.npy") 
print("Array is loaded:",laod_array) # my_array name ka file Load hoga


# example 2
# np.save("file.npy", variable_name/object_name)
np.save("Array_file.npy", array_data)  # Array_file.npy name ka file save hojayega

# np.load("file.npy", variable_name/object_name)
laod_array1 = np.load("Array_file.npy")  
print("Array file loaded:",laod_array1) # Array_file.npy name ka file Load hoga,

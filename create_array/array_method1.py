
import numpy as np

print("Array Reshaping and Flattening:-\n")
# Array Reshaping and Flattening

array1= np.array([1, 2, 3, 4, 5, 6])
        
print("Array:",array1)
print(type(array1))
print("Array Dimetional:", array1.ndim) # Which Type Array?

print("\n" + "=" *25 +"\n")

print("Reshaping Array Method: reshape(6,1) take 2 argument for (total row, total coloum) used kar ke 2D array bana sakte hai\n")                 
# Reshaping Array Method: reshape(6,1) argument pas for (total row, total coloum) used kar ke 2D array bana sakte hai

reshaping = array1.reshape(6,1) # argument pas for (total row, total coloum)

print(reshaping) # reshape output :(6 row, 1 coloum) 
print("Array Dimetional:", reshaping.ndim) # Array type

print()
# Example 1
print("Example 1, Reshaping: variable_reshape_name.reshape(2,3) Method, ( total Row, total Coloum):-")
print(reshaping.reshape(2,3)) # reshape output : (2 row, 3 coloum)
print("Array Dimetional:", reshaping.ndim) # Array type
print()


# Example 2
print("Example 2, (3 row, 2 coloum):-")
print(reshaping.reshape(3,2)) # reshape output : (3 row, 2 coloum)
print("Array Dimetional:", reshaping.ndim) # Which Type Array?
print("\n" + "=" *20 +"\n")

# Flattening
print("Flattening, ka matlab ki aapne pahale rupe me loutna:", reshaping.flatten()) # Flattening, ka matlab ki aapne pahale rupe me loutna
print("Array Dimetional:", array1.ndim) # Which Type Array?
print("\n" + "=" *10 +"\n")

# Array Stacking and Spliting 

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

# Array Stacking
print("Array Stacking Vertical -row wise")
print(np.vstack((a, b))) # Vertical Stacking:- row wise

vr_dim = np.vstack((a, b))
print("Array Dimetional:", vr_dim.ndim) # Which Type Array?
print("\n" + "=" *10 +"\n")

print("Array Stacking Horizontal - Column wise")
print(np.hstack((a, b))) # Horizontal Stack Array:- Column wise

h_dim = np.hstack((a, b))
print("Array Dimetional:", h_dim.ndim) # Which Type Array?
print("\n" + "=" *10 +"\n")

# Array Splitting Horizontal wise
spliting = np.array([[1,2,3,4],[5,6,7,8]])
# type 1
print("Array Splitting Horizontal wise")
print(np.hsplit(spliting, 2))  # Splitting Horizontal wise

# type 2: used for loop
print("\nSplitting Horizontal wise Array") # Splitting Horizontal wise
split_hr = np.hsplit(spliting, 2)
for hr in split_hr:
    print(hr)

print("\n" + "=" *10 +"\n")
# Array Splitting Vertical wise
# type 1
print("Array Splitting Vertical wise")
print(np.vsplit(spliting, 2)) # Splitting Vertical wise

# type 2: used for loop
print("\nSplitting Vertical wise Array")
split_vr = np.vsplit(spliting, 2) # Splitting Vertical wise
for vr in split_vr:
    print(vr)
print("Dimentional array:", vr.ndim)
print("\n" + "=" *10 +"\n")

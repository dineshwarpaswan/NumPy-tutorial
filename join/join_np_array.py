import numpy as np

print("\npython JOIN NumPy Arrays:- With NumPy, we can join  or  add arrays together.\n")

fruits1 = np.array(["APPLE","MANGO","BANANA"])
fruits2 = np.array(["ORANGE","GREPS","KIWI"])

# concatenate() method
fruits = np.concatenate((fruits1, fruits2))
print("My feverate fruits:", fruits)

print()
x =np.array([5, 10, 15])

y= np.array([18, 20, 22])

z = np.array([7, 8, 9])
print(x)
print(y)
print(z)
print()
new_array = np.concatenate((x,y,z))
print("big array:" ,new_array)

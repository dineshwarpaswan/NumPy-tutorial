import numpy as np

print("\npython NumPy Iterate:- Iterate through a NumPy array meance accessing its elements one by one.\n")

fruits = np.array(["APPLE","MANGO","BANANA","ORANGE"])

for f in fruits:
	print("My feverate fruit of:",f)

print()
# nditer(): with for loop

fruits1 = np.array(["APPLE","MANGO","BANANA","ORANGE"])

for fs in np.nditer(fruits1):
        print("My feverate fruit of:",fs)

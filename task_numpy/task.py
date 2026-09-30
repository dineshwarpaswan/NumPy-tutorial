print("\nPROJECT: create 5x5 matrix values from 1to 25, extract last row ,first coloum,mub matrix conttainig 3x3")

import numpy as np 

print("\n1. Create matrix value from 1 to 25 with help of arange(tart,stop) Method:\n")

#1. create 5x5 matrix value with help of arange(Start,stop-1) method:

aran_array= np.arange(1,26)
print(aran_array)
print()

#2. Create 5x5 matrix value with help of reshape(totale row, totale colum) Method:
print("2. Create 5x5 matrix value with help of reshape(totale row, totale colum) Method:\n")

reshape_array = aran_array.reshape(5,5)
print(reshape_array)

#3. extract last row
print("\n3. Extract Last Row:-\n")

last_row = reshape_array[-1:,]
print("Last_row:",last_row)


print("\n3. Extract the firt coloum:-\n")

first_coloum = reshape_array[:,0]
print("first_coloum:", first_coloum)

print("\n3. Extract a 3x3 submatrix(top_left 3x3 region):-\n")

sub_matrix = reshape_array[0:3, 0:3]
print(sub_matrix)


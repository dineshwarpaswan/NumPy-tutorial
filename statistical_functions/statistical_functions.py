print("\nSTATICLA MATHEMATICS FUNCTIONS USED:")
import numpy as np 

# STATICLA MATHEMATICS FUNCTIONS USED:-

statis = np.array([[1,2,3,4],[5,6,7,8]])
print(statis)
print()
print("Sum:", np.sum(statis))
print("Median: ", np.median(statis))
print("Stadian", np.std(statis))
print("Minimum:", np.min(statis))
print("Maximum", np.max(statis))

print("\n" + "=" *10)

print("Array Comparison:-\n")
#Array Comparison
A = np.array([10,20,30])
B = np.array([15,25,30])

print("Array A:" ,A, "\n", "Array B:", B)
print()
print("Comparison of Array A equal to Array B is:",np.array_equal(A, B))  # if all coloum to coloum check value is same vale, result will be: True, nahi to False
print("Compar A == B:", A==B) # Compar all coloum  to coloum but not same result: False 
print("\n" + "=" *15)

# Brodcasting on Array:-
print("# Brodcasting on Array:-")

# example 1
a1 = np.array([5,10,15])
a2 = np.array(5)
print(a1)
print(a2)
print("\nArray a1+ increment Array a2 coloum by coloum = new Array:",a1+a2) # [5,10,15] all coloum me +5 increment, Output new array: [10 15 20]

# example 2
arr_2d = np.array([[10, 20, 30],[20,40,50]])
arr_1d = np.array([5,10,15])

print("2d:",arr_2d,)
print("1d:",arr_1d)
print()
print("brodcasting:",arr_2d + arr_1d)# 2d array me 1d array coloum by colum add hojata hai, output:[[15 30 45][25 50 65]]











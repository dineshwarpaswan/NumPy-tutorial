print("Phthon NumPy data type:- numpy suports greater data types than Phthon does."\
	"\nPhthon suports basic data types: string,int,float,bool,list,tuple,set."\
	"\nNumPy on the other hand, suports these basic data types: bool_,byte,ubyte,int_,intc,uintc,single,double,int8,int16")

import numpy as np 

# dtype Propery
print("\ndtype Propery:- dtype Propery is used to return the data type of a NumPy array.")

int = np.array([1,2,3,4])
print("\ndata type:", int.dtype)

flo = np.array([1.0, 2.4, 3.5, 4.8])
print("\ndata type:", flo.dtype)

s = np.array(["A", "B", "C", "D"])
print("\ndata type:", s.dtype)

bo = np.array([True, False])
print("\ndata type:", bo.dtype)

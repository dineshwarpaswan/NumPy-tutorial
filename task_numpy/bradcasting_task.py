import numpy as np


print("\nTask: Broadcating multiple shape-(3,1) matrix shap-(3,):-\n")

data = np.array([20,40,60])
print("array: ",data)
print()

data1 = data.reshape(3,1)
print("\nreshaping:",data1)


data2 = np.array(5)
print("brodcasting: ",np.array(data1 + data2))


shap= np.array(data1 + data2)
print("\nShape: ",np.shape(shap)) #output (3,1)

print("shape: ",data.shape)


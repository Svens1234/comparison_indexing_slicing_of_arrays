import numpy as np

#int_arr = np.random.randint(0,10,10)
#print(int_arr)
#print(int_arr[0])
#print(int_arr[9])
#print(int_arr[1:3])
#print(int_arr[1:7])
#print(int_arr[0:4])
#print(int_arr[:4])
#print(int_arr[7:10])
#print(int_arr[7:])
#print(int_arr[7:10])
#int_arr[7:10] = 10
#print(int_arr)

arr = np.arange(0,10)
print(arr)
new_arr = arr[:4]
print(new_arr)
new_arr[2:]=7
print(new_arr)
print(arr)
arr1=np.arange(0,10)
print(arr1)
new_arr1=arr1.copy()
print(new_arr1)
new_arr1[:]=0
print(new_arr1)
print(arr1)
print(arr1>3)
bool_arr = arr1>6
print(bool_arr)
print(arr1[bool_arr])
print(arr1[arr1>0])

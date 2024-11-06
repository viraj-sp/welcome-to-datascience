import numpy as np
d_t =[('name','S15'),('class',int),('height',float)]
s_d =[('james',5,48.5),('Nail',6,62.5),('Paul',5,42.10)]
s = np.array(s_d, dtype = d_t)
print("Orignal arry: ")
print(s)
print("sort by height")
print(np.sort(s,order = 'height'))

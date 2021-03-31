import numpy as np

def computeSequence(a, b, x, n):
    sz_a = np.size(a)
    sz_x = np.size(x)
    if(n == sz_x+1):
        _sum = 0
        for i in range(sz_a):
            _sum += a[i]*x[sz_x-1-i]
        _sum += b
        return np.append(x,_sum)
    elif(n > sz_x+1):
        new_x = computeSequence(a,b,x,n-1)
        return computeSequence(a,b,new_x,n)
    elif (n <= sz_x):
        return x[:n]
    
# a = np.array([2.25, -0.5])
# x = np.array([1/3, 1/12])

# print(computeSequence(a,0,x,4))
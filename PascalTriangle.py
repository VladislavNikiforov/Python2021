import numpy as np
n=int(input())
a=np.zeros((n,n))
a[:][0]=1
for i in range(n):
    for j in range(n):
        if j>0 and j<n:
            a[i][j]=a[i-1][j-1]+a[i-1][j]
        else:
            a[i][j]=1
print(a)
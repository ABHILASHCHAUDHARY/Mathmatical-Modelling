import numpy as np
from numpy.linalg import norm

def seidel(a, x ,b):
          
    n = len(a)   

    #calculate x, y , z
    for j in range(0, n):        
        
        temp = b[j]                  

        # calculate xi, yi, zi
        for i in range(0, n):     
            if(j != i):
                temp-=a[j][i] * x[i]
        # updating the value of our solution
        x[j] = temp / a[j][j]
    # returning our updated solution           
    return x    
                
n = 3                             
a = []                            
b = []        
                    
x = [0, 0, 0,0,0,0,0,0,0]
tmp=x
a = [[-4,1,0,1,0,0,0,0,0],
            [1,-4,1,0,1,0,0,0,0],
            [0,1,-4,0,0,1,0,0,0],
            [1,0,0,-4,1,0,1,0,0],
            [0,1,0,1,-4,1,0,1,0],
            [0,0,1,0,1,-4,0,0,1],
            [0,0,0,1,0,0,-4,1,0],
            [0,0,0,0,1,0,1,-4,1],
            [0,0,0,0,0,1,0,1,-4]]
b = [-100,-20,-20,-80,0,0,-260,-180,-180]
#print(x)
print("\nA:\n",a)

print("\nb :\n",b)

print("\nPrinting solution of Ax=b using Gauss siedal method :\n")
itr=1
tol=0.0000001
#loop run for m times depending on m the error value
for i in range(0, 100):            
    x = seidel(a, x, b)
    
print("\nx :\n",x)
        

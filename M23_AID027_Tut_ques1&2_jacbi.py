import numpy as np

#fucntion for jacobi
def jacobi(A,b,N=100,x=None):

    if x is None:
        x = np.zeros(len(A[0]))

#creating a vector of diagonal elements of A 
    D = np.diag(A)

    #subtracting vector D from A
    Z = A - np.diagflat(D)

    for i in range(N):
        x = (b - np.dot(Z,x)) / D
    return x

# A matrix
A = np.array([[-4,1,0,1,0,0,0,0,0],
           [1,-4,1,0,1,0,0,0,0],
            [0,1,-4,0,0,1,0,0,0],
            [1,0,0,-4,1,0,1,0,0],
            [0,1,0,1,-4,1,0,1,0],
            [0,0,1,0,1,-4,0,0,1],
            [0,0,0,1,0,0,-4,1,0],
            [0,0,0,0,1,0,1,-4,1],
            [0,0,0,0,0,1,0,1,-4]])

b = np.array([-100,-20,-20,-80,0,0,-260,-180,-180])
intial_guess = np.array([0,0,0,0,0,0,0,0,0])

sol_x = jacobi(A,b,N=100,x=intial_guess)

print("A:\n")
print(A)

print("b:\n")
print(b)

print("\n SOlution for the x in the equation AX=b using Gauss jacobi method \n")
print(sol_x)
import numpy as np
def obj_fun(x):
    return(350*x[0]+700*x[1]+1400*x[2]-28000)**2

def grad(x):
    return np.array([2*(350*x[0]+700*x[1]+1400*x[2]-28000)*350,2*(350*x[0]+700*x[1]+1400*x[2]-28000)*700,2*(350*x[0]+700*x[1]+1400*x[2]-28000)*1400])
    
def steepest_descent(x0,learning_rate,max_iter,tol):
    for _ in range(max_iter):
        grad=grad(x0)
        if np.linalg.norm(grad)< tol:
            break
        x = x0 - learning_rate * grad
        x0=x
        return x

x0=np.array([1,0,1])
learning_rate=1e-7
max_iter=1000
tol=1e-6
solution=steepest_descent(x0,learning_rate,max_iter,tol)

print("\nNo of 10 m wide tanks :",round(solution[0]))
print("\nNo of 14 m wide tanks :",round(solution[1]))
print("\nNo of 24 m wide tanks :",round(solution[2]))
        
    

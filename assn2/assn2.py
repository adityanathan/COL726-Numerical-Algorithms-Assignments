import numpy as np

def G(n):
    mat = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            mat[i][j] = 2*((i+j+1)%2)/(i+j+1)
    return mat

def dot(p,q):
    leng = p.shape[0]
    return p.T@G(leng)@q

def orthogonalizePolynomials(P):
    V = P
    n = V.shape[1]
    Q = np.zeros(P.shape)
    for i in range(n):
#         rii = dot(V[:,i],V[:,i])
        rii = V[:,i].T@V[:,i]
        Q[:,i] = V[:,i]/rii
        for j in range(i+1, n):
            rij = dot(Q[:,i], V[:,j])
            V[:,j] = V[:,j] - Q[:,i]*rij
    return Q

# orthogonalizePolynomials(np.eye(5))







import numpy as np
def divide11(a,n):
    k=int(n/2)
    #initializing a matrix
    a11=[ [[0] for i in range(0,k)] for j in range(0,k)]
    for i in range(0,k):
        for j in range(0,k):
            a11[i][j]=a[i][j]
    return a11
 
def divide12(a,n):
    k=int(n/2)
    #initializing a matrix
    a12=[ [ [0] for i in range(0,k)]  for j in range(0,k)]
    for i in range(0,k):
        for j in range(0,k):
            a12[i][j]=a[i][j+k]
    return a12
 
def divide21(a,n):
    k=int(n/2)
    #initializing a matrix
    a21=[ [ [0] for i in range(0,k)]  for j in range(0,k)]
    for i in range(0,k):
        for j in range(0,k):
            a21[i][j]=a[i+k][j]
    return a21
 
def divide22(a,n):
    k=int(n/2)
    #initializing a matrix
    a22=[ [ [0] for i in range(0,k)]  for j in range(0,k)]
    for i in range(0,k):
        for j in range(0,k):
            a22[i][j]=a[i+k][j+k]
    return a22
 
def Merge(a11,a12,a21,a22,n):
    k=int(2*n)
    #initializing a matrix
    a = [[[0] for i in range(0, k)] for j in range(0, k)]

    # merging the arrays
    for i in range(0,n):
        for j in range(0,n):
            a[i][j]=a11[i][j]
            a[i][j+n]=a12[i][j]
            a[i+n][j]=a21[i][j]
            a[i+n][j+n]=a22[i][j]
    return a
 
def Plus(a,b,n):
    #initializing a matrix
    c=[[[0] for i in range(0, n)] for j in range(0, n)]

    # adding the elements
    for i in range(0,n):
        for j in range(0,n):
            c[i][j] = a[i][j] + b[i][j]
    return  c
 
def Minus(a,b,n):
    #initializing a matrix
    c=[[[0] for i in range(0, n)] for j in range(0, n)]

    #subtracting the elements
    for i in range(0,n):
        for j in range(0,n):
            c[i][j] = a[i][j] - b[i][j]
    return  c
 
 
def Strassen(a, b, n):
    k = n
    if k == 2:
        d = [[[0] for i in range(2)] for i in range(2)]
        d[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        d[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        d[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        d[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return d
    else:
        a11 = divide11(a, n)
        a12 = divide12(a, n)
        a21 = divide21(a, n)
        a22 = divide22(a, n)
        b11 = divide11(b, n)
        b12 = divide12(b, n)
        b21 = divide21(b, n)
        b22 = divide22(b, n)

        k = int(n / 2)

        m1 = Strassen(a11, Minus(b12, b22, k), k)
        m2 = Strassen(Plus(a11, a12, k), b22, k)
        m3 = Strassen(Plus(a21, a22, k), b11, k)
        m4 = Strassen(a22, Minus(b21, b11, k), k)
        m5 = Strassen(Plus(a11, a22, k), Plus(b11, b22, k), k)
        m6 = Strassen(Minus(a12, a22, k), Plus(b21, b22, k), k)
        m7 = Strassen(Minus(a11, a21, k), Plus(b11, b12, k), k)
 
        c11 = Plus(Minus(Plus(m5, m4, k), m2, k), m6, k)
        c12 = Plus(m1, m2, k)
        c21 = Plus(m3, m4, k)
        c22 = Minus(Minus(Plus(m5, m1, k), m3, k), m7, k)

        c = Merge(c11, c12, c21, c22, k)
        return c
 
 
 
a=np.array([[1,2,3,4],[5,6,7,8],[4,3,2,1],[8,7,6,5]],dtype=int)
b=np.array([[1,2,3,4],[5,6,7,8],[4,3,2,1],[8,7,6,5]],dtype=int)
print(Strassen(a, b, 4))
print("The worse case time complexity of Strassen’s Matrix Multiplication is approximately O(N^2.8074)")

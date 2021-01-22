A = {'a':1,'b':0.9,'c':0.85}
B = {'a':0.9,'b':0.7,'c':0.6}
C = dict()
_A = {}
_B = {}
def Union(A,B):
    for key in A:
        if A[key]>B[key]:
            C[key] = A[key]
        else:
            C[key] = B[key]
    print("A U B :",C)

def Intersection(A,B, f=0):
    for key in A:
        if A[key]<B[key]:
            C[key] = A[key]
        else:
            C[key] = B[key]
    if f == 1:
        return C
    print("A n B :",C)

def Complement(A, f = 0):
    Com = {}
    for key in A:
        Com[key] = round(1-A[key], 2)
    if f == 1:
        return Com
    print('Complement: ', Com)

def Difference(A,B):
    _B = Complement(B , 1)
    C = Intersection(A,_B, f=1)
    print('Difference: ', C)

def Cartesian(A,B):
    r = 0 
    c = 0
    import numpy as np
    C = np.array([0,0,0], ndmin = 2)
    for key_1 in A:
        r = r+1
        c = 0
        for key_2 in B:
            if A[key_1]<B[key_2]:
                C[r][c] = A[key_1]
            else:
                C[r][c] = B[key_2]
            c = c+1
    print('Cartesian Product: ',C)

Union(A,B)
Intersection(A,B)
Complement(A)
Complement(B)
Difference(A,B)
Cartesian(A,B)


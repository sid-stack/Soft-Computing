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

def Cartesian(A,B,f=1):
    r = 0 
    c = 0
    import numpy as np
    C = np.zeros(len(A)*len(B)).reshape(len(A), len(B)) 
    for key_1 in A:
        c = 0
        for key_2 in B:
            if A[key_1]<B[key_2]:
                # C[key_1][key_2] = A[key_1] 
                C[r][c] = A[key_1]
            else:
                # C[key_1][key_2] = B[key_2] 
                C[r][c] = B[key_2]
            c = c+1
        r = r+1
    if f == 0:
        return C
    print('Cartesian Product: \n',C)

def Composition(A,B,C):
    for key_1 in A:
        l = []
        res = []
        for key_2 in B:
            for key_3 in C:
                l.append(max(min(A[key_1],B[key_2]), C[key_3]))
            res.append(max(l))
        print(res)

C = {'a':0.5,'b':0.5,'c':0.5}
Union(A,B)
Intersection(A,B)
Complement(A)
Complement(B)
Difference(A,B)
Cartesian(A,B)
Composition(A,B,C)

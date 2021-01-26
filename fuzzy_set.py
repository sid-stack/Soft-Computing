import numpy as np
A = {'a':1,'b':0.9,'c':0.85}
B = {'a':0.9,'b':0.7,'c':0.6}
C = dict()
X = np.array([[0.5, 0.1],[0.2, 0.9],[0.8,0.6]])
Y = np.array([[0.6,0.4,0.7],[0.5,0.8,0.9]])
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

def Composition(X,Y):
    import numpy as np
    C = np.zeros(X.shape[0]*Y.shape[1]).reshape(X.shape[0], Y.shape[1])
    l = list()
    for i in range(0, X.shape[0]):
        for j in range(0, Y.shape[1]):
            for k in range(0, Y.shape[0]):
                l.append(min(X[i][k], Y[k][j]))
            C[i][j] = max(l)
            l = []
    print('max-min Composition: ', C)
    '''import numpy as np
    C = np.array([[0,1,1],[1,0,0],[0,0,0]])
    l = []
    for i in range(3):
        for j in range(2):
            l.append(float(min(float(X[i][j]), float(Y[j][i]))))

        C[i][j] = float(max(l))
        l = []
    print('max-min Composition: ', C)
'''
Union(A,B)
Intersection(A,B)
Complement(A)
Complement(B)
Difference(A,B)
Cartesian(A,B)
Composition(X,Y)

import math
import datetime
print(datetime.datetime.now().time())
A = [3, 2, 7, 6, 8]

B = [0, 0, 0, 3, 2]

def tongSoMu(A,B):

    lenA = len(A)

    lenB = len(B)

    C = []

    D = []

    for i in range(lenA):

        for j in range(lenB):
            
            D.append(A[i]*B[j])
            
        C.append(D);
        
        D = []

    for i in range(lenA):
        
        for j in range(i):
            
            C[i].insert(0,0)
            
    for i in range(lenA):
        
        j = lenA + lenB -3 - i
        
        while (j > 0):
            
            C[i].append(0)
            
            j -= 1
    s = 0

    t = 0

    T= []

    for i in range(lenA+lenB-1):
        
        for j in range(lenA):
            
            s += C[j][lenA + lenB - 2 - i]

        D.append(s)

        s = 0
        
        t = math.floor((D[i]+t)/10)

        T.append(t)

        if i > 0:

            D[i] = (D[i] + T[i-1] )%10
            
        else:
            
            D[i] = (D[i])%10

    D.append(T[lenB + lenA-2])

    T = []
            
    sumD = sum(D)

    D.reverse()

    print(sumD)

    lenD = len(D)

    for i in range(lenD):
        
        if D[0] != 0:
            
            break
        
        else:
            
            del D[0]
            
    return D

B = tongSoMu(A,B)

A = B

for i in range(4):

    B = tongSoMu(A,B)

A = B
#print(A)
for i in range(9):
    
    B = tongSoMu(B,B)
    
B = []

print(datetime.datetime.now().time())



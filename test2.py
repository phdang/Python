s = 0
B = []
mylist = [1,2,3,4,5,6,7,8,9,10]
Data=[]
import random
while s!= 362880:
    var = []
    Max = 0
    A = [1,1,1,1,1,1,1,1,1,1]
    i1 = random.choice(mylist)
    if i1 not in A:
            A[1]=i1
    i2 = random.choice(mylist)
    if i2 not in A:
            A[2]=i2
        
    i3 = random.choice(mylist)
    if i3 not in A:
            A[3] = i3
                
    i4 = random.choice(mylist)
    if i4 not in A:
            A[4] = i4
                   
    i5 = random.choice(mylist)
    if i5 not in A:
            A[5] = i5
                        
    i6 = random.choice(mylist)
    if i6 not in A:                           
            A[6] = i6
                            
    i7 = random.choice(mylist)
    if i7 not in A:
            A[7]=i7
                                
    i8 = random.choice(mylist)
    if i8 not in A:
            A[8]=i8
                                    
    i9 = random.choice(mylist)
    if i9 not in A:
            A[9]=i9
    if A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9] == 55:
        if A not in B:
            s += 1
            B.append(A)
            var.append(A[8]+A[9]+A[1])
            var.append(A[9] + A[1] +A[2])
            for p in range(8):
                var.append( A[p]+A[p+1]+A[p+2])
            Max = max(var)
            if Max == 18:
                print(A)
           


        




                            
                                
                            
        
    
        

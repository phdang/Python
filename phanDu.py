s= 0
c =0
k=0
p=0
A = []
for i in range (2):
    
    for i1 in range (2):
        
        for i2 in range(2):

            for i3 in range(2):

                for i4 in range(2):

                    for i5 in range(2):

                        for i6 in range(2):

                            for i7 in range(2):

                                A = [i,i1,i2,i3,i4,i5,i6,i7]
                                
                                s += 1

                                if A[0] == 0 and A[1] == 1 and A[7] == 1:
                                

                                    if (i==0 and i==i1) or (i1==0 and i1==i2) or (i2==0 and i2==i3) or (i3 == 0 and i3==i4) or (i4==0 and i4==i5) or (i5==0 and i5==i6) or (i6==0 and i6==i7) or (i7 ==0 and i7 ==i):  

                                            c += 1

                                            print("Truong hop 1:", A)


                                elif A[0] == 1 and A[6] == 1 and A[7] == 0:
                                    

                                    if (i==0 and i==i1) or (i1==0 and i1==i2) or (i2==0 and i2==i3) or (i3 == 0 and i3==i4) or (i4==0 and i4==i5) or (i5==0 and i5==i6) or (i6==0 and i6==i7) or (i7 ==0 and i7 ==i):


                                        k +=1
                                        print("Truong hop 2: ",A)

                                   # else:
#                                            k +=1

#                                            print("Truong hop 3: ", A)
                                            
                                    
                                

                                        
print(s)
print(c)
print(k)
          


 
    
                                    


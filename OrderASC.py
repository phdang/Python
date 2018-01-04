#A = [1002,3,4,7025,9,12,4,300,10,7,1,2,6,8,1,2,4,5,2,6,4,2,8,12,
#     41,24,211,22,330,21,2,35,33,52,12,15,16,19,24,27,
#     47,51,23,555,53,6,80,4000,4,2,7,8,1,22,58,87,98,15,
#     17,-18,-97,12,130,61,29,21,-87,10,24,33,37,48,72,
#     99,3,72,-18,-22,-30,38,65,69,77,8,81,8,102,-1000,
#     -2,-100,-20,30,-40,90,-299,-300,-200,-104,9,0,-8000]
A = [5,7,9,2,4,10,6,8,4,9,1,7,6,8,5,3,10,6,8,4,7,5,7,6,5,6,
     8,3,5,6,1,4,6,8,5,8,7,9,8,6,7,8]
B = []
#A = [8, 2, 3 ,4, 5 ,6 ,7, 1]
lengthA = len(A)
for i in range(lengthA):
    B.append(A[i])
temp = 0
countLoop = 0
i = 0
for i in range(lengthA-1):
    for j in range(i+1,lengthA):
        countLoop += 1
        if A[i] > A[j]:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
print(A)
print(countLoop)
A = B
i = 0
countLoop = 0
while i < lengthA-1:
    countLoop += 1
    if A[i] > A[i+1]:
        temp = A[i]
        A[i] = A[i+1]
        A[i+1] = temp
        if i != 0: 
            i -= 1
        continue
    i += 1
print(A)
print(countLoop)
 
        

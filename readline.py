# Open a file
fo = open("fo.txt", "r+")
b = fo.readlines()
lenb = len(b)
A = []
for i in range(lenb):
    if b[i]== "\n":
        A.append(i)
lenA = len(A)
print(b[0])
print(b[2])
print(b[1])
#for i in range(lenA):
#    for j in range(lenb):
#        if j > A[1] && j < A[2]:
            
# Close opened file
fo.close()

def tong(a,b):
    return a+b
#print(5 * tong(3+1,2))
x= input('nhap x: ')
y = input('nhap y: ')
z = input('nhap z: ')
if (x > y) and (x > z):
    a, b, c = x, y, z
elif (y > x) and (y > z):
    a = y, b = x, c = z;
elif (z > x) and (z > y):
    a, b, c = z, x, y
print(a,b,c)
3

vuongCan = ""

n = int(input("Nhap so canh cua tam giac vuong can: "))

#So canh tam giac vuong can phai > 1

if n > 1:

    for i in range(n):
        
        for j in range(n):
            
            if (i == j or i == 0 or j == n - 1):
                
                vuongCan += " *"
                
            else:
                
                vuongCan += "  "
                
        vuongCan += "\n"
        
    print(vuongCan)
    
# So canh cua tam giac khong hop le khi <= 1

else :
    
    print("So canh khong hop le !")

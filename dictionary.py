import random
dapan = {'2+3':'5', "2+4":'6', "5+6":'11'}
cauhoi = ['2+3', '2+4', '5+6']
Ans = random.randint(1, 3) - 1
cauHoi = cauhoi[Ans]
dapAn = dapan[cauHoi]
print(cauHoi)
traloi = input()

if traloi == dapAn:
    print("dung")
else:
    print("sai")

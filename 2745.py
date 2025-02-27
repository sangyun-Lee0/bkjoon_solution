N, B = input().split()
B = int(B)
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
deci = 0
for i in range(len(N),0, -1):
    deci += num.index(N[len(N)-i])*B**(i-1)
print(deci) 

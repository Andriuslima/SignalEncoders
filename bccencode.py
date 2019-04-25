import sys
arg=str(sys.argv[1])
i=0
a=bin(0)
L=[]
for c in arg:
    L.append(bin(ord(c)))
    i+=1
bs=str(a)

it=0
for num in L:
    cont=0
    for c in num: 

        if(c=='1'): 
            cont+=1
    
    num = int(num, 2)
    num = num<<1
    if(cont%2==1):
        num=num|1
    L[it]=bin(num)    
    it+=1

horizontal=[]   
for i in range(8):
    horizontal.append('0')
    for j in range(len(L)):
        if(L[j][i+2]=='1'):
            if(horizontal[i]!='1'):
                
                horizontal[i]='1'
            else:
                horizontal[i]='0'

final="0b"  
for i in horizontal:
    final+=i
L.append(final)
final=""
for i in L:
    final+=str(hex(int(i,2)))[2:]
print(final)


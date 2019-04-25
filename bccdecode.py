import sys
arg=str(bin(int(str(sys.argv[1]),16)))
#print(arg)
L=[]
for i in range(len(arg)//8):
    L.append(arg[2+i*8:2+(i+1)*8])
#print(L)


for i in L:
    c='0'
    for j in range(8):
        if(i[j]=='1'):
            if(c=='0'):
                c='1'
            else:
                c='0'
    if(c!='0'):
        print("erro")
        quit()
for i in range(len(L)-1):
    print(chr(int(L[i][0:-1],2)),end='')

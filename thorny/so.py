f=open('C:/Users/admin/Desktop/in.inp.txt','r')
y=open('C:/Users/admin/Desktop/out.out.txt','w')
dayso= f.readline().split()
tong = 0 
mang=[]
for i in range(1,int(dayso[1])+1):
    for j in range(int(dayso[0]),int(dayso[1])+1):
        if j%i == 0 and i not in mang :
            tong += i
            mang.append(i)
print(tong)
y.write(str(tong))
f.close()
y.close()



    

    
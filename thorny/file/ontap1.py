vao = open('C:/Users/admin/Desktop/in.inp.txt','r')
ra = open('C:/Users/admin/Desktop/out.out.txt','w')
mang = vao.read().split()
tong = 0
x = mang[-1]
n = mang[0]
del mang[-1]
del mang[0]
for i in range(0,int(n)-1):
    for j in range(i+1,int(n)):
        if (int(mang[i]) + int(mang[j]) == int(x)) and (1 <= (i+1) < (j+1) <= int(n)) :
            tong +=1
ra.write(str(tong))
vao.close()
ra.close()

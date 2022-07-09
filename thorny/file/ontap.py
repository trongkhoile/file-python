dulieu = open('C:/Users/admin/Documents/tailwind/vao.inp.txt','r')
daura = open('C:/Users/admin/Documents/tailwind/ra.out.txt','w')
mang= dulieu.read().split()
sotoado = mang[0]
solonnhat = 0
del mang[0]
mangmoi=[]
for i in range(0,len(mang),2):
    mangcon = [mang[i],mang[i+1]]
    mangmoi.append(mangcon)
print(mangmoi)
for i in range(0,len(mangmoi)-1):
    for j in range(i+1,len(mangmoi)):
        if (abs(int(mangmoi[i][0]) - int(mangmoi[j][0]))+abs(int(mangmoi[i][1]) - int(mangmoi[j][1]))) > solonnhat :
            solonnhat = (abs(int(mangmoi[i][0]) - int(mangmoi[j][0]))+abs(int(mangmoi[i][1]) - int(mangmoi[j][1])))
daura.write(str(solonnhat))
dulieu.close()
daura.close()

    
        
mangcaccanho =[100,150,150,200 ,250 , 300 , 250,150, 400,150,500,150,600,700,800]
mangcaccanho.sort()
mangrong = []
mangchua=[]
dem=0
socantim=0
print(mangcaccanho)
i=0
while i < len(mangcaccanho):
    if mangcaccanho[i] not in mangrong :
        mangrong.append(mangcaccanho[i])
    i+=1
print(mangrong)
print(len(mangrong))
k=0
while k < len(mangrong) :
    mangchua.append(mangcaccanho.count(mangrong[k]))
    k+=1

m=0
while m < len(mangcaccanho):
    if mangcaccanho.count(mangcaccanho[m])==max(mangchua):
              socantim=mangcaccanho[m]
    m+=1
print("")
print("",socantim,"",max(mangchua))

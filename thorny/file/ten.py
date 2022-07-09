def run():
    a = float(input("Nhập số a :"))
    b = float(input("Nhập số b :"))
    c = float(input("Nhập số c :"))
    denta = b**2 - 4*a*c 
    if a==0 and b ==0 and c== 0 :
        print("Phương trình có vô số nghiệm")
    elif a==0 and b ==0 and c>0:
        print("Phương trình vô nghiệm ")
    elif denta > 0 :
        print("Phương trình có nghiệm kép ")
    elif denta < 0 :
        print("Phương trình vô nghiệm")
    elif denta == 0 :
        print("Phương trình có nghiệm kép ")
run()
    
        
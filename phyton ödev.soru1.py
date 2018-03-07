#x=finansmanGelir,y=pazarGelir,z=kiraGelir
def f(x,y,z):
    m=x+y+z
    return m
#a=ucret,b=finansmanGider,c=pazarGiderleri,d=kiraGiderleri,e=muhasebeGiderleri
def f(a,b,c,d,e):
    g=a+b+c+d+e
    return g
#toplamGelir=m,toplamGider=g
m=int(input("hesaplanan gelir toplamını giriniz"))
g=int(input("hesaplanan gider toplamını giriniz"))
t=m-g
if t==1000:
    print('işletme başabaş noktasında')
elif t>1000:
    print('işletme kar elde eder')
else:
    print('işletme zarar eder')

    
    

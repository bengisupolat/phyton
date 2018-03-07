#a=planlamısÜretimSüresi,b=plansızDurus
def f(a,b):
    x=(a-b)/a
    return x
#c=standartCevrimZamanı,d=üretimMiktari,a=planmısÜretimSüresi,b=plansızDurus
def f(c,d,a,b):
    y=(c*d)/(a-b)
    return y
#e=sağlamÜrünMiktari,g=toplamÜretimMiktari
def f(e,g):
    z=e/g
    return z
#x=kullanılabilirlik,y=performans,z=kalite
def f(x,y,z):
    t=(x*y*z)*1/100
    return t

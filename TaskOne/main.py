import math
from random import random

# Задание 1
def calc_pi(x0, y0, r0, ExperimentsNum):
    x_min, y_min = x0 - r0, y0 - r0
    x_max, y_max = x0 + r0, y0 + r0
    m = 0
    for i in range(ExperimentsNum):
        x = (x_max - x_min) * random() + x_min
        y = (y_max - y_min) * random() + y_min

        if (x - x0) ** 2 + (y - y0) ** 2 < r0 ** 2:
            m = m + 1

    return m / ExperimentsNum * 4


#Задание 2
Pi = calc_pi(x0=1, y0=1, r0=5, ExperimentsNum=10 ** 4)
print("Pi = " + str(Pi))

ExpNumbers = (10**4, 10**5, 10**6, 10**7, 10**8)
Seria_1 = [calc_pi(1,2,5,i) for i in ExpNumbers]
print("Значения Пи для 1 серии: "+ str(Seria_1))

Seria_2 = [calc_pi(1,2,5,i) for i in ExpNumbers]
print("Значения Пи для 2 серии: "+str(Seria_2))

Seria_3 = [calc_pi(1,2,5,i) for i in ExpNumbers]
print("Значения Пи для 3 серии: "+ str(Seria_3))

Seria_4 = [calc_pi(1,2,5,i) for i in ExpNumbers]
print("Значения Пи для 4 серии: "+ str(Seria_4))

Seria_5 = [calc_pi(1,2,5,i) for i in ExpNumbers]
print("Значения Пи для 1 серии: "+ str(Seria_5))


#Задание 3
Eps1 = list(map(lambda x: abs((x-math.pi)/math.pi), Seria_1))
Eps2 = list(map(lambda x: abs((x-math.pi)/math.pi), Seria_2))
Eps3 = list(map(lambda x: abs((x-math.pi)/math.pi), Seria_3))
Eps4 = list(map(lambda x: abs((x-math.pi)/math.pi), Seria_4))
Eps5 = list(map(lambda x: abs((x-math.pi)/math.pi), Seria_5))
print("Погрешности: ")
print(str(Eps1) + "\n" + str(Eps2) + "\n" + str(Eps3) + "\n" + str(Eps4) + "\n" + str(Eps5)+"\n")

S_e4 = (Seria_1[0]+Seria_2[0]+Seria_3[0]+Seria_4[0]+Seria_5[0])/5
Eps_S_e4 = abs((S_e4-math.pi)/math.pi)

S_e5 = (Seria_1[1]+Seria_2[1]+Seria_3[1]+Seria_4[1]+Seria_5[1])/5
Eps_S_e5 = abs((S_e5-math.pi)/math.pi)

S_e6 = (Seria_1[2]+Seria_2[2]+Seria_3[2]+Seria_4[2]+Seria_5[2])/5
Eps_S_e6 = abs((S_e6-math.pi)/math.pi)

S_e7 = (Seria_1[3]+Seria_2[3]+Seria_3[3]+Seria_4[3]+Seria_5[3])/5
Eps_S_e7 = abs((S_e7-math.pi)/math.pi)

S_e8 = (Seria_1[4]+Seria_2[4]+Seria_3[4]+Seria_4[4]+Seria_5[4])/5
Eps_S_e8 = abs((S_e8-math.pi)/math.pi)


print("Средние результаты по 5 сериям для каждой: "+"\n"+str(S_e4)+"\t"+str(S_e5)+"\t"+str(S_e6)+
      "\t"+str(S_e7)+"\t"+str(S_e8)+"\n")

print("погрешности вычислений для усредненого значения: "+"\n"+str(Eps_S_e4) +
      "\t"+ str(Eps_S_e5)+"\t"+ str(Eps_S_e6)+"\t"+ str(Eps_S_e6)+"\t"+
      str(Eps_S_e7)+ "\t"+str(Eps_S_e8)+"\n")


#Задание 4
def f(x):
    return (x**3+1)

def calc_integral(a,b,f,ExperimentsNumb):
    m = 0
    x_min = a
    x_max = b
    y_min = 0
    y_max = f(b)
    for i in range(ExperimentsNumb):
        x = (x_max - x_min) * random() + x_min
        y = ( y_max - y_min) * random() + y_min

        if f(x) > y:
            m = m + 1

    return m / ExperimentsNumb * (b - a) * f(b)

Seria1 = [calc_integral(0,2,f,i) for i in(ExpNumbers)]
print("Значения интеграла для 1 серии: "+ str(Seria1))

Seria2 = [calc_integral(0,2,f,i) for i in(ExpNumbers)]
print("Значения интеграла для 2 серии: "+ str(Seria2))

Seria3 = [calc_integral(0,2,f,i) for i in(ExpNumbers)]
print("Значения интеграла для 3 серии: "+ str(Seria3))

Seria4 = [calc_integral(0,2,f,i) for i in(ExpNumbers)]
print("Значения интеграла для 4 серии: "+ str(Seria4))

Seria5 = [calc_integral(0,2,f,i) for i in(ExpNumbers)]
print("Значения интеграла для 5 серии: "+ str(Seria5)+"\n")

eps1 = list(map(lambda x: abs((x-6)/6), Seria1))
eps2 = list(map(lambda x: abs((x-6)/6), Seria2))
eps3 = list(map(lambda x: abs((x-6)/6), Seria3))
eps4 = list(map(lambda x: abs((x-6)/6), Seria4))
eps5 = list(map(lambda x: abs((x-6)/6), Seria5))

print("Погрешности:")
print(str(eps1)+ "\n"+str(eps2)+ "\n"+str(eps3)+ "\n"+str(eps4)+ "\n"+str(eps5)+"\n")

S_E4 = (Seria1[0]+Seria2[0]+Seria3[0]+Seria4[0]+Seria5[0])/5
Eps_S_E4 = abs((S_E4-6)/6)

S_E5 = (Seria1[1]+Seria2[1]+Seria3[1]+Seria4[1]+Seria5[1])/5
Eps_S_E5 = abs((S_E5-6)/6)

S_E6 = (Seria1[2]+Seria2[2]+Seria3[2]+Seria4[2]+Seria5[2])/5
Eps_S_E6 = abs((S_E6-6)/6)

S_E7 = (Seria1[3]+Seria2[3]+Seria3[3]+Seria4[3]+Seria5[3])/5
Eps_S_E7 = abs((S_E7-6)/6)

S_E8 = (Seria1[4]+Seria2[4]+Seria3[4]+Seria4[4]+Seria5[4])/5
Eps_S_E8 = abs((S_E8-6)/6)

print("Средние результаты по 5 сериям для каждой: "+"\n"+str(S_E4)+
      "\t"+str(S_E5)+"\t"+str(S_E6)+
      "\t"+str(S_E7)+"\t"+str(S_E8)+"\n")

print("погрешности вычислений для усредненого значения: "+"\n"+str(Eps_S_e4)
      +"\t"+ str(Eps_S_e5)+"\t"+ str(Eps_S_e6)+"\t"+
      str(Eps_S_e7)+"\t"+ str(Eps_S_e8))

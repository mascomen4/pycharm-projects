import math
import cmath
print("{0:-^80}".format(" Корни квадратного уравнения "))
a = b = c = 0
def quadratic():
    while True:
        try:
            a = float(input("Введите коэфициэнт при x*x: "))
            if a == 0:
                print("0 запрещен. Попробуйте заново")
                continue
            b = float(input("Введите коэфициэнт при x: "))
            c = float(input("Введите свободный коэффициэнт: "))
        except ValueError as err:
            print("Вы ввели неверный символ. Попробуйте заново")
            continue
        disc = b**2 - 4*a*c
        if disc >=0:
            if disc == 0:
                x1 = -b/2*a
                print("Корень уравнения : x=", x1)
            elif disc>0:
                x1 = -b + math.sqrt(disc)/2*a
                x2 = -b - math.sqrt(disc)/2*a
                print("Корни квадртаного уравнения: x1 =", x1, "x2 =", x2)
        else:
            x1 = -b + cmath.sqrt(disc)/2*a
            x2 = -b - cmath.sqrt(disc)/2*a
            print("{0}x\N{superscript two} + {1}x + {2} \N{rightwards arrow} x1 =".format(a,b,c), x1, "x2 =", x2)
        break

while True:
        quadratic()
        print("{0:-^80}".format("Для повтора нажмите 1. Для выходя любой символ "), end = "\n")
        x = int(input())
        if x == 1: continue
        else: break

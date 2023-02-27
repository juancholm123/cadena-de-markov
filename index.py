import math

print("Ingrese la cantidad de usaurios")
n = int(input())


def binomial_coefficient(n, x):
    return math.comb(n, x)


def recorrer():
    p = 0.3
    acum = 0
    for i in range(n+1):

        for x in range(n+1):
            pro = binomial_coefficient(n, x) * p**x * (1-p)**(n-x)
            acum = acum + pro
           
            print("p" + str(i) + str(x) + " = " + "[" + str(pro) + "]", end=" ")

            if (x == n):
                print("Suma[" + str(acum) + "]", end=" ")
                acum=0
        print()


recorrer()

from RandomNumberGenerator import RandomNumberGenerator
import math
import copy
from timeit import default_timer as timer


def clear_bit(value, bit):
    return value & ~(1 << bit)


def show(pi, p, w, d):
    C = []
    T = []
    wT = []
    j = 0
    Cstart = 0
    wiTi = 0
    for x in pi:
        Cstart = Cstart + p[x - 1]
        C.append(Cstart)
    for x in pi:
        Tstart = max(C[j] - d[x - 1], 0)
        wTstart = w[x - 1] * Tstart
        wiTi = wiTi + wTstart
        T.append(Tstart)
        wT.append(wTstart)
        j = j + 1
    print("C: ", C)
    print("T: ", T)
    print("wT: ", wT)


def main():
    seed = int(input("Podaj seed "))
    random = RandomNumberGenerator(seed)
    n = int(input("Podaj ilosc zadan "))
    nr = []
    pi = []
    p = []
    w = []
    d = []
    for i in range(1, n + 1):
        p.append(random.nextInt(1, 29))
        nr.append(i)
    A = sum(p)
    for _ in range(n):
        w.append(random.nextInt(1, 9))
    for _ in range(n):
        d.append(random.nextInt(1, 29))

    print("nr: ", nr)
    print("p: ", p)
    print("w: ", w)
    print("d: ", d)
    power_n = pow(2, n)
    D = range(1, power_n)
    memory = [0] * power_n
    minidx = [0] * power_n
    start = timer()
    for i in D:
        binary = [int(x) for x in bin(i)[2:]]
        binary.reverse()
        D_short = [x for x, val in enumerate(binary) if val]
        suma = 0
        memory[i] = math.inf
        for j in D_short:
            suma = suma + p[j]
        for j in D_short:
            x = clear_bit(i, j)
            value = max(suma - d[j], 0) * w[j] + memory[x]
            if value < memory[i]:
                memory[i] = value
                minidx[i] = j + 1

    pi.append(minidx[power_n - 1])
    x = power_n - 1
    for _ in range(n-1):
        x = clear_bit(x, pi[-1]-1)
        pi.append(minidx[x])
    pi.reverse()
    end = timer()
    print("Dynamic programming: ")
    print("pi: ", pi)
    show(pi, p, w, d)
    print("Funkcja celu: ", memory[power_n - 1])
    print("Czas dzialania: ", end - start, " s")


main()

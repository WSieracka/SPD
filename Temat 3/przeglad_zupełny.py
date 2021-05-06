from RandomNumberGenerator import RandomNumberGenerator
import math
import copy

pi_opt = []  # optymalna kolejnosc wykonywania zadan
p_org = []
w = []
d = []
C = []
T = []
wT = []
UB_bf = math.inf
def printcalculate(pi):
    C = []
    T = []
    wT = []
    j=0
    Cstart = 0
    wiTi = 0
    for x in pi:
        Cstart = Cstart + p_org[x - 1]
        C.append(Cstart)
    for x in pi:
        Tstart = max(C[j]-d[x-1],0)
        wTstart = w[x - 1] * Tstart
        wiTi = wiTi + wTstart
        T.append(Tstart)
        wT.append(wTstart)
        j = j+1
    print("C: ", C)
    print("T: ", T)
    print("wT: ", wT)
def calculate(pi):
    C = []
    T = []
    wT = []
    j=0
    Cstart = 0
    wiTi = 0
    for x in pi:
        Cstart = Cstart + p_org[x - 1]
        C.append(Cstart)
    for x in pi:
        Tstart = max(C[j]-d[x-1],0)
        wTstart = w[x - 1] * Tstart
        wiTi = wiTi + wTstart
        T.append(Tstart)
        wT.append(wTstart)
        j = j+1
    return wiTi
def bf(x, N, pi, n):
    global UB_bf
    global pi_opt_bf
    global p_org
    global pi_opt
    pi.append(x)
    N.remove(x)
    if N:
        for y in N:
            r = copy.deepcopy(pi)
            K = copy.deepcopy(N)
            bf(y, K, r, n)
    else:
        wiTi = calculate(pi)
        if wiTi < UB_bf:
            UB_bf = wiTi
            pi_opt = pi


def main():
    global pi_opt
    global p_org
    global w
    global d
    seed = int(input("Podaj seed "))
    random = RandomNumberGenerator(seed)
    n = int(input("Podaj rozmiar "))
    ranging = range(1, n + 1)

    nr = []

    for i in ranging:
        p_org.append(random.nextInt(1, 29))
        nr.append(i)

    for i in ranging:
        w.append(random.nextInt(1, 9))

    #A = sum(p)
    for _ in ranging:
        d.append(random.nextInt(1, 29))

    print("n:", n)
    print("nr:", nr)
    print("p:", p_org)
    print("w:", w)
    print("d:", d)
    N = list(nr)
    for x in N:
        K = copy.deepcopy(N)
        pi = []
        bf(x, K, pi, n)
    print("pi: ", pi_opt)
    printcalculate(pi_opt)
    print("wiTi sum: ", UB_bf)


main()
from RandomNumberGenerator import RandomNumberGenerator
import math
import copy

pi_opt = []  # optymalna kolejnosc wykonywania zadan
p_org = []
pi_opt_bf = []
UB = math.inf
UB_bf = math.inf
m = 0
n = 0
licznik = 0
licznik_bf = 0


def min_i(m, p, N):
    minimum = p[N[0] - 1][0]
    indeks = 0
    ranging = [0, m - 1]
    for j in N:
        for i in ranging:
            if minimum > p[j - 1][i]:
                minimum = p[j - 1][i]
                indeks = i
    return indeks


def min_j(m, p, N):
    minimum = p[N[0] - 1][0]
    zadanie = N[0]
    ranging = [0, m - 1]
    for j in N:
        for i in ranging:
            if minimum > p[j - 1][i]:
                minimum = p[j - 1][i]
                zadanie = j
    return zadanie


def print_c(pi):
    C = [[0] * m for _ in range(n)]
    start = 0
    j = 0
    for x in pi:
        start = start + p_org[x - 1][0]
        C[j][0] = start
        j = j + 1
    ranging = range(1, m)
    for i in ranging:
        j = 0
        for x in pi:
            if j != 0:
                C[j][i] = max(C[j - 1][i], C[j][i - 1]) + p_org[x - 1][i]
            else:
                C[j][i] = C[j][i - 1] + p_org[x - 1][i]
            j = j + 1
    Cmax = C[n - 1][m - 1]
    print("pi: ", pi)
    print("C: ", C)
    print("Cmax: ", Cmax)


def calculate(pi):
    C = [[0] * m for _ in range(n)]
    start = 0
    j = 0
    for x in pi:
        start = start + p_org[x - 1][0]
        C[j][0] = start
        j = j + 1
    ranging = range(1, m)
    for i in ranging:
        j = 0
        for x in pi:
            if j != 0:
                C[j][i] = max(C[j - 1][i], C[j][i - 1]) + p_org[x - 1][i]
            else:
                C[j][i] = C[j][i - 1] + p_org[x - 1][i]
            j = j + 1
    Cmax = C[n - 1][m - 1]
    return Cmax


def bound_calculate(pi, machine):
    C = [[0] * m for _ in range(n)]
    start = 0
    j = 0
    for x in pi:
        start = start + p_org[x - 1][0]
        C[j][0] = start
        j = j + 1
    ranging = range(1, machine)
    for i in ranging:
        j = 0
        for x in pi:
            if j != 0:
                C[j][i] = max(C[j - 1][i], C[j][i - 1]) + p_org[x - 1][i]
            else:
                C[j][i] = C[j][i - 1] + p_org[x - 1][i]
            j = j + 1
    Cmax = C[len(pi) - 1][machine - 1]
    return Cmax


def johnson(p_given, nr):
    p = copy.deepcopy(p_given)
    # if m > 2:
    # sr = m // 2
    # for i in range(n):
    # p[i][0] = p[i][0] + p[i][sr]
    # p[i][m - 1] = p[i][m - 1] + p[i][sr]
    l = 0
    pi = []
    pi_end = []
    N = copy.deepcopy(nr)
    C = [[0] * m for _ in range(n)]
    while N:
        indeks = min_i(m, p, N)
        zadanie = min_j(m, p, N)
        if indeks == 0:
            pi.insert(l, zadanie)
            l = l + 1
        else:
            pi_end.append(zadanie)
        N.remove(zadanie)
    pi_end.reverse()
    a = len(pi_end)
    for i in range(a):
        pi.append(pi_end[i])

    start = 0
    j = 0
    for x in pi:
        start = start + p_org[x - 1][0]
        C[j][0] = start
        j = j + 1
    ranging = range(1, m)
    for i in ranging:
        j = 0
        for x in pi:
            if j != 0:
                C[j][i] = max(C[j - 1][i], C[j][i - 1]) + p_org[x - 1][i]
            else:
                C[j][i] = C[j][i - 1] + p_org[x - 1][i]
            j = j + 1
    Cmax = C[n - 1][m - 1]

    print("Johnson")
    print("pi: ", pi)
    print("C: ", C)
    print("Cmax: ", Cmax)
    return Cmax, pi


# wykorzystano wzor Lb4
def bound(pi_given, N):
    LB = 0
    pi = copy.deepcopy(pi_given)
    for i in range(m):
        total = bound_calculate(pi, i)
        amount = 0
        for x in N:
            amount = amount + p_org[x - 1][i]
        total = total + amount
        if i < m-1:
            minim = math.inf
        else:
            minim = 0
        for j in N:
            amount = 0
            for k in range(i + 1, m):
                amount = amount + p_org[j - 1][k]
            if amount < minim:
                minim = amount
        total = total + minim
        if total > LB:
            LB = total
    return LB


def bf(x, N, pi, n, m):
    global UB_bf
    global pi_opt_bf
    global p_org
    global licznik_bf
    pi.append(x)
    N.remove(x)
    if N:
        for y in N:
            r = copy.deepcopy(pi)
            K = copy.deepcopy(N)
            bf(y, K, r, n, m)
    else:
        licznik_bf = licznik_bf + 1
        Cmax = calculate(pi)
        if Cmax < UB_bf:
            UB_bf = Cmax
            pi_opt_bf = pi


def bnb(x, N, pi, n, m):
    global UB
    global pi_opt
    global p_org
    global licznik
    pi.append(x)
    N.remove(x)
    if N:
        LB = bound(pi, N)
        if LB < UB:
            for y in N:
                r = copy.deepcopy(pi)
                K = copy.deepcopy(N)
                bnb(y, K, r, n, m)
    else:
        licznik = licznik + 1
        Cmax = calculate(pi)
        if Cmax < UB:
            UB = Cmax
            pi_opt = pi


def main():
    global n
    global m
    global UB
    global UB_bf
    global pi_opt
    global pi_opt_bf
    global p_org
    seed = int(input("Podaj seed "))
    random = RandomNumberGenerator(seed)
    n = int(input("Podaj ilosc zadan "))
    m = int(input("Podaj liczbe maszyn "))
    ranging = range(1, n + 1)
    nr = []
    p_org = [[0] * m for _ in range(n)]  # wykonywanie
    for j in range(n):
        for i in range(m):
            p_org[j][i] = random.nextInt(1, 29)
    for i in ranging:
        nr.append(i)
    print("p:", p_org)

    UB, pi_opt = johnson(p_org, nr)

    N = list(nr)
    for x in N:
        K = copy.deepcopy(N)
        pi = []
        bf(x, K, pi, n, m)
    print("pi: ", pi_opt_bf)
    print("Cmax: ", UB_bf)

    N = list(nr)
    for x in N:
        K = copy.deepcopy(N)
        pi = []
        bnb(x, K, pi, n, m)
    print("pi: ", pi_opt)
    print("Cmax: ", UB)

    print("licznik bf: ", licznik_bf)
    print("licznik: ", licznik)


main()

from RandomNumberGenerator import RandomNumberGenerator
import math
import copy

pi_opt = []  # optymalna kolejnosc wykonywania zadan
p_org = []
w = []
d = []



def min_index(K, N):
    minimum = K[N[0] - 1]
    index = N[0] - 1
    for i in N:
        if minimum > K[i - 1]:
            minimum = K[i - 1]
            index = i - 1
    return index

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
    N = copy.deepcopy(nr)
    K = copy.deepcopy(d)
    Sd = []
    Sw = []
    Sp = []
    Snr = []
    #Sd, Sw, Sp, Snr=zip(*[(x,y,z,k) for x,y,z,k in sorted(zip(d,w,p_org,nr))])

    while N:
        j = min_index(K, N)
        Sd.append(d[j])
        Sw.append(w[j])
        Sp.append(p_org[j])
        Snr.append(j + 1)
        N.remove(j + 1)
    d=list(Sd)
    w=list(Sw)
    p_org=list(Sp)
    pi=list(Snr)

    C = []
    T = []
    wT = []
    j=0
    Cstart = 0
    wiTi = 0
    for x in nr:
        Cstart = Cstart + p_org[x - 1]
        C.append(Cstart)
    for x in nr:
        Tstart = max(C[j]-d[x-1],0)
        wTstart = w[x - 1] * Tstart
        wiTi = wiTi + wTstart
        T.append(Tstart)
        wT.append(wTstart)
        j = j+1
    print("pi: ", pi)
    print("C: ", C)
    print("T: ", T)
    print("wT: ", wT)
    print("wiTi: ", wiTi)

main()

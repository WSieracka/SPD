from RandomNumberGenerator import RandomNumberGenerator
import math
import copy

pi_opt = []  # optymalna kolejnosc wykonywania zadan
pi_org = []
UB = math.inf


def min_value(r, N):
    minimum = r[N[0] - 1]
    for i in N:
        if minimum > r[i - 1]:
            minimum = r[i - 1]
    return minimum


def min_index(r, N):
    minimum = r[N[0] - 1]
    index = N[0] - 1
    for i in N:
        if minimum > r[i - 1]:
            minimum = r[i - 1]
            index = i - 1
    return index


def max_value(q, G):
    maximum = q[G[0] - 1]
    for i in G:
        if maximum < q[i - 1]:
            maximum = q[i - 1]
    return maximum


def max_index(q, G):
    maximum = q[G[0] - 1]
    index = G[0] - 1
    for i in G:
        if maximum < q[i - 1]:
            maximum = q[i - 1]
            index = i - 1
    return index


def schrage(r, p, q, pi):
    nr = list(pi)
    G = []
    N = list(nr)
    pi = []
    Cq = []
    t = min(r)

    Cmax = 0
    while G or N:
        while N and min_value(r, N) <= t:
            j = min_index(r, N)
            G.append(j + 1)
            N.remove(j + 1)
        if G:
            j = max_index(q, G)
            G.remove(j + 1)
            pi.append(nr[j])
            t = t + p[j]
            Cq.append(t + q[j])
            Cmax = max(Cmax, max(Cq))
        else:
            t = min_value(r, N)

    return Cmax, pi


def schragepmtn(r, p, q, pi):
    nr = list(pi)
    G = []
    N = list(nr)
    pi = []
    a = 0
    p_left = list(p)
    t = min(r)
    Cmax = 0

    while N and min_value(r, N) <= t:
        j = min_index(r, N)
        G.append(j + 1)
        N.remove(j + 1)

    while G or N:
        while N and min_value(r, N) <= t:
            j = min_index(r, N)
            G.append(j + 1)
            N.remove(j + 1)
            if q[j] > q[a]:
                left = t - r[j]
                t = r[j]
                if left > 0:
                    G.append(a + 1)
                    p_left[a] = left
        if G:
            j = max_index(q, G)
            G.remove(j + 1)
            a = j
            pi.append(nr[j])
            t = t + p_left[j]
            Cmax = max(Cmax, t + q[j])
        else:
            t = min_value(r, N)

    return Cmax


def carlier(r, p, q):
    global UB
    U, pi = schrage(r, p, q, pi_org)  # kolejnosc zadan wg algorytmu schrage
    if U < UB:  # jesli Cmax zwrocony przez schrage jest mniejszy od gornej granicy to zamieniamy
        UB = U
        global pi_opt
        pi_opt = list(pi)
    # szukamy dla jakiego zadania jest Cmax, bedzie to naszym b (ostatnie zadanie na sciezce krytycznej)
    S = []
    C = []
    S.append(r[pi[0] - 1])
    C.append(S[-1] + p[pi[0] - 1])
    Cmax = C[-1] + q[pi[0] - 1]
    b = pi[0] - 1  # numer zadania b
    for j in pi[1:]:
        S.append(max(r[j - 1], C[-1]))
        C.append(S[-1] + p[j - 1])
        if Cmax <= C[-1] + q[j - 1]:
            Cmax = C[-1] + q[j - 1]
            b = j
    b_index = pi.index(b)
    a = -1
    # szukamy pierwszego zadania na sciezce krytycznej a
    for j in pi:
        p_sum = 0
        j_index = pi.index(j)
        for k in pi[j_index:b_index + 1]:
            p_sum = p_sum + p[k - 1]
        if Cmax == (r[j - 1] + p_sum + q[b - 1]):
            a = j  # numer zadania a
            break
    if a == -1:
        return None
    a_index = pi.index(a)
    b_index = pi.index(b)
    if a_index >= b_index:  # sprawdzamy czy mamy dwa elementy w przedziale <a,b)
        return None
    c = -1
    # szukamy czy istnieje zadanie c ktore ma mniejsze q niz q(b)
    for j in pi[a_index:b_index + 1]:
        if q[j - 1] < q[b - 1]:
            c = j  # numer zadania c
            break
    if c == -1:  # jesli nie zostalo znalezione zadanie c to wracamy
        return None
    # szukamy zadania c o jak najwyzszej pozycji i mniejszym q niz q(b)
    for j in pi[a_index:b_index + 1]:
        if q[j - 1] < q[b - 1]:
            c = j
    c_index = pi.index(c)
    K = []
    if c_index + 1 >= len(pi):
        return None
    elif c_index + 1 == b_index:  # jesli tylko jedno zadanie w przedziale
        K.append(pi[b_index])
    else:
        K = pi[c_index + 1:b_index + 1]  # tworzymy zbior zadan K z zadan (c+1,b)
    r1 = min_value(r, K)
    q1 = min_value(q, K)
    p1 = 0
    for i in K:
        p1 = p1 + p[i - 1]
    r_old = copy.deepcopy(r[c - 1])  # zapisujemy stara wartosc r
    r[c - 1] = max(r[c - 1], r1 + p1)
    LB = schragepmtn(r, p, q, pi_org)
    # jesli czas zwrocony przez schragepmtn ze zmnienionym r jest mniejszy niz gorne oszacowanie to wywolujemy carlier
    if LB < UB:
        carlier(r, p, q)
    r[c - 1] = copy.deepcopy(r_old)  # przywracamy stara wartosc r
    q_old = copy.deepcopy(q[c - 1])  # zapisujemy stara wartosc q
    q[c - 1] = max(q[c - 1], q1 + p1)
    LB = schragepmtn(r, p, q, pi_org)
    # jesli czas zwrocony przez schragepmtn ze zmienionym q jest mniejszy niz gorne oszacowanie to wywolujemy carlier
    if LB < UB:
        carlier(r, p, q)
    q[c - 1] = copy.deepcopy(q_old)  # przywracamy stara wartosc q


def main():
    seed = int(input("Podaj seed "))
    random = RandomNumberGenerator(seed)
    n_org = int(input("Podaj rozmiar "))
    ranging = range(1, n_org + 1)

    nr_org = []  # numer
    r_org = []  # przygotowywanie
    p_org = []  # wykonywanie
    q_org = []  # stygniecie

    for i in ranging:
        p_org.append(random.nextInt(1, 29))
        nr_org.append(i)

    global pi_org
    pi_org = list(nr_org)
    A = sum(p_org)
    for _ in ranging:
        r_org.append(random.nextInt(1, A))
    for _ in ranging:
        q_org.append(random.nextInt(1, A))
    print("n:", n_org)
    print("nr:", nr_org)
    print("r:", r_org)
    print("p:", p_org)
    print("q:", q_org)
    carlier(r_org, p_org, q_org)
    print("Kolejnosc:", pi_opt)

    S = []
    C = []
    S.append(r_org[pi_opt[0] - 1])
    C.append(S[-1] + p_org[pi_opt[0] - 1])
    Cmax = C[-1] + q_org[pi_opt[0] - 1]
    for j in pi_opt[1:]:
        S.append(max(r_org[j - 1], C[-1]))
        C.append(S[-1] + p_org[j - 1])
        if Cmax < C[-1] + q_org[j - 1]:
            Cmax = C[-1] + q_org[j - 1]
    print("Cmax: ", Cmax)


main()

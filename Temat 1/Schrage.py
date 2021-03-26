from RandomNumberGenerator import RandomNumberGenerator


# funkcja zwracajaca wartosc najmniejszego czasu przygotowania ze zbioru zadan N
def min_value(r, N):
    minimum = r[N[0] - 1]
    for i in N:
        if minimum > r[i - 1]:
            minimum = r[i - 1]
    return minimum


# funkcja zwracaja indeks najmniejszego czasu przygotowania ze zbioru zadan N
def min_index(r, N):
    minimum = r[N[0] - 1]
    index = N[0] - 1
    for i in N:
        if minimum > r[i - 1]:
            minimum = r[i - 1]
            index = i - 1
    return index


# funkcja zwracajaca wartosc najwiekszego czasu stygniecia ze zbioru zadan G
def max_value(q, G):
    maximum = q[G[0] - 1]
    for i in G:
        if maximum < q[i - 1]:
            maximum = q[i - 1]
    return maximum


# funkcja zwracajaca indeks najwiekszego czasu stygniecia ze zbioru zadan G
def max_index(q, G):
    maximum = q[G[0] - 1]
    index = G[0] - 1
    for i in G:
        if maximum < q[i - 1]:
            maximum = q[i - 1]
            index = i - 1
    return index


def main():
    seed = int(input("Podaj seed "))
    random = RandomNumberGenerator(seed)
    n = int(input("Podaj rozmiar "))
    ranging = range(1, n + 1)

    nr = []  # numer
    r = []  # przygotowywanie
    p = []  # wykonywanie
    q = []  # stygniecie

    for i in ranging:
        p.append(random.nextInt(1, 29))
        nr.append(i)

    A = sum(p)
    for _ in ranging:
        r.append(random.nextInt(1, A))
    for _ in ranging:
        q.append(random.nextInt(1, A))
    print("n:", n)
    print("nr:", nr)
    print("r:", r)
    print("p:", p)
    print("q:", q)

    G = []  # lista gotowych zadan
    N = list(nr)  # zbior zadan niegotowych
    pi = []  # kolejnosc wykonywania zadan
    S = []  # czas rozpoczecia
    C = []  # czas zakonczenia
    Cq = []  # czas zakonczenia i stygniecia
    t = min(r)  # chwila czasowa

    Cmax = 0
    while G or N:
        while N and min_value(r, N) <= t:  # szukamy gotowych zadan
            j = min_index(r, N)  # zapisujemy indeks zadania o najmniejszym czasie przygotowania
            G.append(j + 1)  # dodajemy gotowe zadanie
            N.remove(j + 1)  # usuwanie gotowe zadanie
        if G:
            j = max_index(q, G)  # zapisujemy indeks zadania o najwiekszym czasie stygniecia
            G.remove(j + 1)  # usuwamy zadanie ktore zostalo wykonane
            pi.append(nr[j])  # dodajemy numer zadania do kolejnosci
            S.append(t)  # zapisujemy czas rozpoczecia
            t = t + p[j]  # powiekszamy chwile czasowa o czas wykonania
            C.append(t)  # zapisujemy czas zakonczenia
            Cq.append(t + q[j])  # zapisujemy czas zakonczenia + stygniecia
            Cmax = max(Cmax, max(Cq))  # zapisujemy max czas zakonczenia
        else:
            t = min_value(r, N)  # czekamy az bedzie jakies zadanie gotowe

    print("pi:", pi)
    print("S: ", S)
    print("C: ", C)
    print("Cq: ", Cq)
    print("Cmax: ", Cmax)


main()

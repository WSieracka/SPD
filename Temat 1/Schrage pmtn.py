from RandomNumberGenerator import RandomNumberGenerator
import math


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
    C = []  # czas zakonczenia
    a = 0  # aktualnie wykonywane zadanie
    p_left = list(p)
    t = min(r)  # chwila czasowa
    Cmax = 0

    while N and min_value(r, N) <= t:
        j = min_index(r, N)
        G.append(j + 1)
        N.remove(j + 1)

    while G or N:
        while N and min_value(r, N) <= t:  # szukamy gotowych zadan
            j = min_index(r, N)  # zapisujemy indeks zadania o najmniejszym czasie przygotowania
            G.append(j + 1)  # dodajemy gotowe zadanie
            N.remove(j + 1)  # usuwanie gotowe zadanie
    # sprawdzamy czy nie istnieje jakies gotowe zadanie o czasie stygniecia krotszym niz aktualnie wykonywanego zadnaia
            if q[j] > q[a]:
                left = t - r[j]  # przypisujemy czas ktory pozostal do wykonania zadania
                t = r[j]  # przypisujemy odpowiednia chwile czasowa
                if left > 0:  # jesli zadanie jeszcze ma czas to musimy je z powrotem dodac do listy gotowych zadan
                    G.append(a + 1)
                    C.pop()  # usuwamy jego czas zakonczenia
                    C.append(t)  # dodajemy zmieniony czas zakoczenia
                    p_left[a] = left  # zapisujemy pozostaly czas wykonania
        if G:
            j = max_index(q, G)  # zapisujemy indeks zadania o najwiekszym czasie stygniecia
            G.remove(j + 1)  # usuwamy zadanie ktore zostalo wykonane
            a = j  # indeks aktualnie wykonywanego zadania
            pi.append(nr[j])  # dodajemy numer zadania do kolejnosci
            t = t + p_left[j]  # powiekszamy chwile czasowa o czas wykonania
            C.append(t)  # zapisujemy czas zakonczenia
            Cmax = max(Cmax, t + q[j])  # zapisujemy max czas zakonczenia
        else:
            t = min_value(r, N)  # czekamy az bedzie jakies zadanie gotowe

    print("pi:", pi)
    print("C: ", C)
    print("Cmax: ", Cmax)


main()

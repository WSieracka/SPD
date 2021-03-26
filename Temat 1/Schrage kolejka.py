from RandomNumberGenerator import RandomNumberGenerator


# klasa zadanie przechowujaca parametry danego zadania
class Zadanie:
    def __init__(self, nr, r, p, q):
        self.nr = nr
        self.r = r
        self.p = p
        self.q = q

    def show(self):
        print("Nr:", self.nr, "r:", self.r, "p:", self.p, "q:", self.q, )


# kolejka z priorytetem wg parametru czasu przygotowania
class RPriorityQueue:
    def __init__(self):
        self.list = []

    def dodaj(self, zad):
        wpisano = 0
        if not self.list:  # jesli pusta lista to po prostu wpisujemy zadanie
            self.list.append(zad)
        else:
            for i in self.list:  # przeszukujemy liste zeby wpisac w odpowiednie miejsce
                if zad.r < i.r:
                    indeks = self.list.index(i)
                    self.list = self.list[0:indeks] + [zad] + self.list[
                                                              indeks:]  # dodajemy zadanie w odpowiednim miejscu
                    wpisano = 1
                    break
            if not wpisano:  # jesli to najwiekszy element to dodajemy go na koniec
                self.list.append(zad)

    def pokaz(self):
        print("nr: ")
        for i in self.list:
            print(i.nr, end=" ")
        print("\nr: ")
        for i in self.list:
            print(i.r, end=" ")
        print("\np: ")
        for i in self.list:
            print(i.p, end=" ")
        print("\nq: ")
        for i in self.list:
            print(i.q, end=" ")
        print("\n")


# kolejka z priorytetem wg parametru czasu stygniecia
class QPriorityQueue:
    def __init__(self):
        self.list = []

    def dodaj(self, zad):
        wpisano = 0
        if not self.list:
            self.list.append(zad)
        else:
            for i in self.list:
                if zad.q < i.q:
                    indeks = self.list.index(i)
                    self.list = self.list[0:indeks] + [zad] + self.list[indeks:]
                    wpisano = 1
                    break
            if not wpisano:
                self.list.append(zad)

    def pokaz(self):
        print("nr: ")
        for i in self.list:
            print(i.nr, end=" ")
        print("\nr: ")
        for i in self.list:
            print(i.r, end=" ")
        print("\np: ")
        for i in self.list:
            print(i.p, end=" ")
        print("\nq: ")
        for i in self.list:
            print(i.q, end=" ")
        print("\n")


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

    Q = RPriorityQueue()
    N = RPriorityQueue()
    for i in ranging:
        Q.dodaj(Zadanie(nr[i - 1], r[i - 1], p[i - 1], q[i - 1]))
        N.dodaj(Zadanie(nr[i - 1], r[i - 1], p[i - 1], q[i - 1]))
    Q.list.reverse()
    N.list.reverse()
    Q.pokaz()
    G = QPriorityQueue()
    pi = []
    S = []
    C = []
    Cq = []
    t = N.list[-1].r

    Cmax = 0
    while G.list or N.list:
        while N.list and N.list[-1].r <= t:
            zadanie = N.list.pop()
            G.dodaj(zadanie)
        if G.list:
            current = G.list.pop()
            pi.append(current.nr)
            S.append(t)
            t = t + current.p
            C.append(t)
            Cq.append(t + current.q)
            Cmax = max(Cmax, max(Cq))
        else:
            t = N.list[-1].r

    print("pi:", pi)
    print("S: ", S)
    print("C: ", C)
    print("Cq: ", Cq)
    print("Cmax: ", Cmax)


main()

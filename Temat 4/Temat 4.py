from RandomNumberGenerator import RandomNumberGenerator
import math
import copy

pi_opt = []


def calculate(pi, n, m, p_org, operations, if_print=0):
    m_floor = math.floor(m * 1.2) + 1
    C = [[0] * m_floor for _ in range(n)]
    op = copy.deepcopy(operations)
    prev_op = 0
    #print(pi)
    while op!=0:
        if prev_op == op:
            return math.inf
        machine = 0
        prev_op = copy.deepcopy(op)
        for row in pi:
            if len(pi[machine])>0:
                if C[pi[machine][0][0]-1][pi[machine][0][1]-1] == 0:
                    if pi[machine][0][1] != 1:
                        if C[pi[machine][0][0] - 1][pi[machine][0][1] - 2] != 0:
                            S = C[pi[machine][0][0] - 1][pi[machine][0][1] - 2]
                            op = op - 1
                            C[pi[machine][0][0]-1][pi[machine][0][1]-1] = S + p_org[pi[machine][0][0]-1][pi[machine][0][1]-1]
                    else:
                        op = op - 1
                        C[pi[machine][0][0] - 1][pi[machine][0][1] - 1] = p_org[pi[machine][0][0] - 1][pi[machine][0][1]-1]
                x = 1

                for z in row[1:]:
                    if C[pi[machine][x][0] - 1][pi[machine][x][1] - 1] == 0:
                        if pi[machine][x][1] == 1 and C[pi[machine][x - 1][0] - 1][pi[machine][x - 1][1] - 1] !=0:
                            S = C[pi[machine][x - 1][0] - 1][pi[machine][x - 1][1] - 1]
                            op = op - 1
                            C[pi[machine][x][0]-1][pi[machine][x][1]-1] = S + p_org[pi[machine][x][0]-1][pi[machine][x][1]-1]
                        elif C[pi[machine][x][0] - 1][pi[machine][x][1] - 2] != 0 and C[pi[machine][x - 1][0] - 1][pi[machine][x - 1][1] - 1] !=0:
                            S = max(C[pi[machine][x][0] - 1][pi[machine][x][1] - 2],
                                    C[pi[machine][x - 1][0] - 1][pi[machine][x - 1][1] - 1])
                            C[pi[machine][x][0]-1][pi[machine][x][1]-1] = S + p_org[pi[machine][x][0]-1][pi[machine][x][1]-1]
                            op = op - 1
                    x = x + 1

            machine = machine + 1
    Cmax = 0
    for machine in pi:
        if len(machine)>0:
            if C[machine[-1][0]-1][machine[-1][1]-1] > Cmax:
                Cmax = C[machine[-1][0]-1][machine[-1][1]-1]
    if if_print:
        print("pi: ", pi)
        print("C: ", C)
        print("Cmax: ", Cmax)
    else:
        #print(Cmax)
        #print(C)
        return Cmax


def main():
    global pi_opt
    seed = int(input("Podaj seed "))
    random = RandomNumberGenerator(seed)
    n = int(input("Podaj ilosc zadan "))
    m = int(input("Podaj liczbe maszyn "))
    ranging = range(1, n + 1)
    nr = []
    o = [0] * n
    m_floor = math.floor(m * 1.2) + 1
    p_org = [[0] * m_floor for _ in range(n)]  # wykonywanie
    u = [[0] * m_floor for _ in range(n)]
    operations = 0
    for j in range(n):
        o[j] = random.nextInt(2, m_floor)
        operations = operations + o[j]
        for i in range(o[j]):
            p_org[j][i] = random.nextInt(1, 29)
    for j in range(n):
        for i in range(o[j]):
            u[j][i] = random.nextInt(1, m)
    for i in ranging:
        nr.append(i)
    print("p:", p_org)
    print("u: ", u)
    k = [0] * m
    W = nr.copy()
    first_op = [0] * n
    pi = [[] for _ in range(m)]
    pi_opt = copy.deepcopy(pi)
    op = 0
    while W:
        max_val = 0
        max_op = (0, 0)
        for i in W:
            if p_org[i - 1][first_op[i - 1]] > max_val:
                max_val = p_org[i - 1][first_op[i - 1]]
                max_op = (i, first_op[i - 1]+1)
        first_op[max_op[0]-1] = first_op[max_op[0]-1] + 1
        if first_op[max_op[0]-1] == o[max_op[0]-1]:
            W.remove(max_op[0])
        op = op + 1
        l = 0
        idx = 0
        for x in pi[u[max_op[0]-1][max_op[1]-1]-1]:
            idx = idx + 1
            if x[0] == max_op[0]:
                l = idx
        pi_opt[u[max_op[0]-1][max_op[1]-1] - 1].insert(l, max_op)
        l = l + 1
        while l <= k[u[max_op[0]-1][max_op[1]-1] - 1]:
            cal_pi = copy.deepcopy(pi)
            cal_pi[u[max_op[0]-1][max_op[1]-1]-1].insert(l, max_op)
            if calculate(cal_pi, n, m, p_org, op) < calculate(pi_opt, n, m, p_org, op):
                pi_opt = copy.deepcopy(cal_pi)
            l = l + 1
        pi = copy.deepcopy(pi_opt)
        k[u[max_op[0]-1][max_op[1]-1] - 1] = k[u[max_op[0]-1][max_op[1]-1] - 1] + 1
    #print("pi: ", pi_opt)
    calculate(pi_opt, n, m, p_org, operations, 1)


main()

from RandomNumberGenerator import RandomNumberGenerator
import math
import copy
import random

pi_opt_insa = []


def calculate(pi, n, m, p_org, operations, if_print=0):
    m_floor = math.floor(m * 1.2) + 1
    C = [[0] * m_floor for _ in range(n)]
    op = copy.deepcopy(operations)
    prev_op = 0
    # print(pi)
    while op != 0:
        if prev_op == op:
            return math.inf
        machine = 0
        prev_op = copy.deepcopy(op)
        for row in pi:
            if len(pi[machine]) > 0:
                if C[pi[machine][0][0] - 1][pi[machine][0][1] - 1] == 0:
                    if pi[machine][0][1] != 1:
                        if C[pi[machine][0][0] - 1][pi[machine][0][1] - 2] != 0:
                            S = C[pi[machine][0][0] - 1][pi[machine][0][1] - 2]
                            op = op - 1
                            C[pi[machine][0][0] - 1][pi[machine][0][1] - 1] = S + p_org[pi[machine][0][0] - 1][
                                pi[machine][0][1] - 1]
                    else:
                        op = op - 1
                        C[pi[machine][0][0] - 1][pi[machine][0][1] - 1] = p_org[pi[machine][0][0] - 1][
                            pi[machine][0][1] - 1]
                x = 1

                for z in row[1:]:
                    if C[pi[machine][x][0] - 1][pi[machine][x][1] - 1] == 0:
                        if pi[machine][x][1] == 1 and C[pi[machine][x - 1][0] - 1][pi[machine][x - 1][1] - 1] != 0:
                            S = C[pi[machine][x - 1][0] - 1][pi[machine][x - 1][1] - 1]
                            op = op - 1
                            C[pi[machine][x][0] - 1][pi[machine][x][1] - 1] = S + p_org[pi[machine][x][0] - 1][
                                pi[machine][x][1] - 1]
                        elif C[pi[machine][x][0] - 1][pi[machine][x][1] - 2] != 0 and C[pi[machine][x - 1][0] - 1][
                            pi[machine][x - 1][1] - 1] != 0:
                            S = max(C[pi[machine][x][0] - 1][pi[machine][x][1] - 2],
                                    C[pi[machine][x - 1][0] - 1][pi[machine][x - 1][1] - 1])
                            C[pi[machine][x][0] - 1][pi[machine][x][1] - 1] = S + p_org[pi[machine][x][0] - 1][
                                pi[machine][x][1] - 1]
                            op = op - 1
                    x = x + 1

            machine = machine + 1
    Cmax = 0
    for machine in pi:
        if len(machine) > 0:
            if C[machine[-1][0] - 1][machine[-1][1] - 1] > Cmax:
                Cmax = C[machine[-1][0] - 1][machine[-1][1] - 1]
    if if_print:
        print("pi: ", pi)
        print("C: ", C)
        print("Cmax: ", Cmax)
    else:
        # print(Cmax)
        # print(C)
        return Cmax


def move(pi, i_m, i, j):
    new_pi = copy.deepcopy(pi)
    a = new_pi[i_m][i][0]
    b = new_pi[i_m][i][1]
    new_pi[i_m][i] = new_pi[i_m][j]
    new_pi[i_m][j] = (a, b)
    return new_pi


def main():
    global pi_opt_insa
    seed = int(input("Podaj seed "))
    rand_gen = RandomNumberGenerator(seed)
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
        o[j] = rand_gen.nextInt(2, m_floor)
        operations = operations + o[j]
        for i in range(o[j]):
            p_org[j][i] = rand_gen.nextInt(1, 29)
    for j in range(n):
        for i in range(o[j]):
            u[j][i] = rand_gen.nextInt(1, m)
    for i in ranging:
        nr.append(i)
    print("p:", p_org)
    print("u: ", u)
    k = [0] * m
    W = nr.copy()
    first_op = [0] * n
    pi = [[] for _ in range(m)]
    pi_opt_insa = copy.deepcopy(pi)
    op = 0
    while W:
        max_val = 0
        max_op = (0, 0)
        for i in W:
            if p_org[i - 1][first_op[i - 1]] > max_val:
                max_val = p_org[i - 1][first_op[i - 1]]
                max_op = (i, first_op[i - 1] + 1)
        first_op[max_op[0] - 1] = first_op[max_op[0] - 1] + 1
        if first_op[max_op[0] - 1] == o[max_op[0] - 1]:
            W.remove(max_op[0])
        op = op + 1
        l = 0
        idx = 0
        for x in pi[u[max_op[0] - 1][max_op[1] - 1] - 1]:
            idx = idx + 1
            if x[0] == max_op[0]:
                l = idx
        pi_opt_insa[u[max_op[0] - 1][max_op[1] - 1] - 1].insert(l, max_op)
        l = l + 1
        while l <= k[u[max_op[0] - 1][max_op[1] - 1] - 1]:
            cal_pi = copy.deepcopy(pi)
            cal_pi[u[max_op[0] - 1][max_op[1] - 1] - 1].insert(l, max_op)
            if calculate(cal_pi, n, m, p_org, op) < calculate(pi_opt_insa, n, m, p_org, op):
                pi_opt_insa = copy.deepcopy(cal_pi)
            l = l + 1
        pi = copy.deepcopy(pi_opt_insa)
        k[u[max_op[0] - 1][max_op[1] - 1] - 1] = k[u[max_op[0] - 1][max_op[1] - 1] - 1] + 1
    # print("pi: ", pi_opt_insa)
    calculate(pi_opt_insa, n, m, p_org, operations, 1)

    pi = copy.deepcopy(pi_opt_insa)
    pi_opt = copy.deepcopy(pi_opt_insa)
    T = 200
    T_reduce = 10
    while T > 0:
        for k in range(100):
            i_m = random.randint(0, m - 1)
            i = random.randint(0, len(pi_opt_insa[i_m]) - 1)
            j = random.randint(0, len(pi_opt_insa[i_m]) - 1)
            pi_new = move(pi, i_m, i, j)
            pi_new_Cmax = calculate(pi_new, n, m, p_org, operations)
            if pi_new_Cmax != math.inf:
                delta_Cmax = calculate(pi, n, m, p_org, operations) - pi_new_Cmax
                if delta_Cmax < 0:
                    r = random.uniform(0, 1)
                    if r >= math.exp(delta_Cmax / T):
                        pi_new = pi
                pi = pi_new
                if calculate(pi, n, m, p_org, operations) < calculate(pi_opt, n, m, p_org, operations):
                    pi_opt = copy.deepcopy(pi)
        T = T - T_reduce
    calculate(pi_opt, n, m, p_org, operations, 1)
    Cmax_ref = calculate(pi_opt_insa, n, m, p_org, operations, 0)
    Cmax = calculate(pi_opt, n, m, p_org, operations, 0)
    prd = (Cmax - Cmax_ref)/Cmax_ref * 100
    print("PRD: ", prd)


main()

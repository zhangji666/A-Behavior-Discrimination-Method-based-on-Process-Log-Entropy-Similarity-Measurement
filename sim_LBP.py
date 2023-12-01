import fun
from scipy.optimize import linprog
import pandas as pd

list = []
log0 = pd.read_csv('E://张纪//方老师//17个日志//Log_P0.csv', index_col=0)
# print(log0)
for i in range(1, 18):
# for i in range(1, 2):
    temp = []
    log = pd.read_csv('E://张纪//方老师//17个日志//Log_P' + str(i) + '.csv', index_col=0)
    # print(log)
    #  计算min
    for r0 in log0.iterrows():
        # print("*" * 99)
        trace_log0 = r0[1]['trace']
        # print(trace_log0)
        for r in log.iterrows():
            trace_log = r[1]['trace']
            # print(trace_log)
            l = fun.d_seq(trace_log0, trace_log)
            l = '%.3f' % l
            temp.append(l)

    matrix = []
    #  ***************************
    T_1 = []
    for r0 in log0.iterrows():
        # print("*" * 99)
        pi = r0[1]['frequency'] / 1000
        T_1.append('%.3f' % pi)
    # print(T_1)
    for x1 in range(len(log0)):
        A = [0] * (len(log) * len(log0))
        for x2 in range(len(log)):
            A[x2 + len(log) * x1] = 1
        matrix.append(A)
        # print(A)
    # ********************
    T_2 = []
    for r0 in log.iterrows():
        # print("*" * 99)
        pi = r0[1]['frequency'] / 1000
        T_2.append('%.3f' % pi)
    # print(T_2)
    for x1 in range(len(log)):
        A = [0] * (len(log) * len(log0))
        for x2 in range(len(log0)):
            A[x1 + len(log) * x2] = 1
        matrix.append(A)
        # print(A)
    b = T_1 + T_2
    beq = []
    Aeq = matrix
    for cv in b:
        beq.append([float(cv)])
    LB = [0] * (len(temp))
    UB = [None] * len(temp)
    bound = tuple(zip(LB, UB))
    # print('temp', temp)
    # print(len(temp))
    # for cx in Aeq:
    #     print(cx)
    # print(len(Aeq))
    # print('beq', beq)
    # print(len(beq))
    # print('bound', bound)
    # print(len(bound))
    # print("log0:", len(log0))
    # print("log:", len(log))
    res = linprog(c=temp, A_eq=Aeq, b_eq=beq, bounds=bound)
    word = "LogP0和LogP" + str(i) + "相似度"
    list.append([word, '%.3f' % (1 - res.fun)])
for i in list:
    print(i)


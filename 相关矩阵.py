from fun import *
import pandas as pd
import numpy as np
import scipy.stats


def set_of_activity(log0):
    '''
    生成矩阵的索引
    :param log0: log0 = pd.read_csv('E://张纪//方老师//17个日志//Log_P0.csv', index_col=0)
    :return: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    '''
    l0 = daoru(log0)
    l0 = toSAP(l0)
    activity = []
    for i in range(len(l0[0])):
        s = ','.join(l0[0][i])
        s = s.split(",")
        activity.append(s[0])
        activity.append(s[1])
    activity = list(dict.fromkeys(activity))
    activity = sorted(activity, key=str.lower)
    # print(activity)
    return activity


def to_matrix(log0):
    '''

    :param log0:
    :return:     A      B      C      D      E      F      G
            A  0.0  324.0  245.0  431.0    0.0    0.0    0.0
            B  0.0    0.0    0.0  324.0  185.0    0.0    0.0
            C  0.0    0.0    0.0  245.0  246.0    0.0    0.0
            D  0.0  185.0  246.0    0.0  569.0    0.0    0.0
            E  0.0    0.0    0.0    0.0    0.0  653.0  347.0
            F  0.0    0.0    0.0    0.0    0.0    0.0    0.0
            G  0.0    0.0    0.0    0.0    0.0    0.0    0.0
    '''
    activity = set_of_activity(log0)
    matrix = pd.DataFrame(np.zeros((len(activity), len(activity))), index=activity, columns=activity)
    l0 = daoru(log0)
    l0 = toSAP(l0)
    l = len(l0[0])
    l0 = pd.DataFrame(l0)
    # print(l0)
    for i in range(l):
        act = l0.loc[0, i]
        p = l0.loc[1, i]
        # print(act, p)
        act = ','.join(act)
        act = act.split(",")
        s, e = act[0], act[1]
        matrix.loc[s, e] = p
    # print(matrix)
    return matrix


def to_RMatrix(matrix):
    '''
    将频率矩阵转化为度量矩阵
    :param matrix:      A      B      C      D      E      F      G
                    A  0.0  324.0  245.0  431.0    0.0    0.0    0.0
                    B  0.0    0.0    0.0  324.0  185.0    0.0    0.0
                    C  0.0    0.0    0.0  245.0  246.0    0.0    0.0
                    D  0.0  185.0  246.0    0.0  569.0    0.0    0.0
                    E  0.0    0.0    0.0    0.0    0.0  653.0  347.0
                    F  0.0    0.0    0.0    0.0    0.0    0.0    0.0
                    G  0.0    0.0    0.0    0.0    0.0    0.0    0.0
    :return:           A         B         C         D         E         F         G
                A  0.000000  0.996923  0.995935  0.997685  0.000000  0.000000  0.000000
                B -0.499230  0.000000  0.000000  0.272549  0.994624  0.000000  0.000000
                C -0.498982  0.000000  0.000000 -0.002033  0.995951  0.000000  0.000000
                D -0.499421  0.991705  0.995968  0.000000  0.998246  0.000000  0.000000
                E  0.000000 -0.498652 -0.498986 -0.499561  0.000000  0.998471  0.997126
                F  0.000000  0.000000  0.000000  0.000000 -0.499617  0.000000  0.000000
                G  0.000000  0.000000  0.000000  0.000000 -0.499281  0.000000  0.000000

    '''
    set = matrix.columns
    m = pd.DataFrame(np.zeros((len(set), len(set))), index=set, columns=set)
    for i in range(len(set)):
        s = set[i]
        for j in range(len(set)):
            e = set[j]
            if s == e:
                m.loc[s, e] = matrix.loc[s, e] / (matrix.loc[s, e] + 1)
            else:
                m.loc[s, e] = (matrix.loc[s, e] - matrix.loc[e, s]) / (matrix.loc[s, e] + matrix.loc[e, s] + 1)
    return m


def ComIndex(log1, log2):
    '''
    生成两日志公共活动索引
    :param log1:
    :param log2:
    :return:
    '''
    index1 = set_of_activity(log1)
    index2 = set_of_activity(log2)
    index = list(dict.fromkeys(index1 + index2))
    index = sorted(index, key=str.lower)
    return index


def ComMatrix(log1, log2):
    '''
    计算两个日志的公共活动索引的度量矩阵
    :param log1:
    :param log2:
    :return: m1,m2两个度量矩阵
    '''
    activity = ComIndex(log1, log2)
    m1 = pd.DataFrame(np.zeros((len(activity), len(activity))), index=activity, columns=activity)
    m2 = pd.DataFrame(np.zeros((len(activity), len(activity))), index=activity, columns=activity)
    matrix1 = to_matrix(log1)
    matrix2 = to_matrix(log2)
    matrix1 = to_RMatrix(matrix1)
    matrix2 = to_RMatrix(matrix2)

    for i in range(len(matrix1.columns)):
        s = matrix1.columns[i]
        for j in range(len(matrix1.columns)):
            e = matrix1.columns[j]
            m1.loc[s, e] = matrix1.loc[s, e]
    # print(m1)
    for i in range(len(matrix2.columns)):
        s = matrix2.columns[i]
        for j in range(len(matrix2.columns)):
            e = matrix2.columns[j]
            m2.loc[s, e] = matrix2.loc[s, e]
    # print(m2)
    return m1, m2


def matrix2pandn(m1):
    """
    将度量矩阵m1的正负值分开
    :param m1:
    :return:
    """
    m1_positive = pd.DataFrame(np.zeros((len(m1.columns), len(m1.columns))), index=m1.columns, columns=m1.columns)
    m1_negative = pd.DataFrame(np.zeros((len(m1.columns), len(m1.columns))), index=m1.columns, columns=m1.columns)
    for i in m1.columns:
        s = i
        for j in m1.columns:
            e = j
            if m1.loc[s, e] > 0:
                m1_positive.loc[s, e] = m1.loc[s, e]
            else:
                m1_negative.loc[s, e] = m1.loc[s, e]
    m1_negative = abs(m1_negative)
    # print(m1_positive)
    # print(m1_negative)
    return m1_positive, m1_negative


def addepsilon(l, e=10 ** -7):
    """
    将数组中为0值的位置添加e
    :param l:
    :param e:
    :return:
    """
    zero = 0
    l = np.array(l)
    for col in l:
        if col == 0:
            zero += 1
    num = len(l)
    if num == zero:
        l += e
    else:
        for i in range(len(l)):
            if l[i] == 0:
                l[i] += e
            else:
                l[i] -= zero * e / (num - zero)
    return l


def similarity(m1, m2):
    """
    计算活动相关性
    :param m1:相关矩阵1
    :param m2:相关矩阵2
    :return:
    """
    s = []
    for i in m1.columns:
        set1 = m1.loc[i, :]
        set2 = m2.loc[i, :]
        set1 = addepsilon(np.array(set1))
        set2 = addepsilon(np.array(set2))
        set1 = set1 / sum(set1)
        set2 = set2 / sum(set2)
        M = (set1 + set2) / 2
        js = 0.5 * scipy.stats.entropy(set1, M) + 0.5 * scipy.stats.entropy(set2, M)
        s.append(round(1 - js, 3))
    print(pd.DataFrame([s], columns=m1.columns))


def sim_activity(log0, log11):
    """
    用similarity(m1_p, m2_p)计算日志活动正负相关性
    :param log0:
    :param log11:
    :return:
    """
    m1, m2 = ComMatrix(log0, log11)
    m1_p, m1_n = matrix2pandn(m1)
    m2_p, m2_n = matrix2pandn(m2)
    print('活动正相关性')
    similarity(m1_p, m2_p)
    print('活动负相关性')
    similarity(m1_n, m2_n)


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)
    log0 = pd.read_csv('E://张纪//方老师//17个日志//Log_P0.csv', index_col=0)
    log = pd.read_csv('E://张纪//方老师//17个日志//Log_P17.csv', index_col=0)

    l0 = daoru(log0)
    l0 = toSAP(l0)
    l = daoru(log)
    l = toSAP(l)
    Seq = SeqAPMS(l0, l)
    print('%.3f' % Seq)

    m1, m2 = ComMatrix(log0, log)
    print(m1)
    print(m2)
    m1_p, m1_n = matrix2pandn(m1)
    m2_p, m2_n = matrix2pandn(m2)
    m1_p.to_csv('E://张纪//方老师//卷积行为区分//data.txt', sep=',', index=False, header=False)
    print('m1_p')
    print(m1_p.applymap(lambda x: '%.5f' % x))
    print('m2_p')
    print(m2_p.applymap(lambda x: '%.5f' % x))
    print('m1_n')
    print(m1_n.applymap(lambda x: '%.5f' % x))
    print('m2_n')
    print(m2_n.applymap(lambda x: '%.5f' % x))
    sim_activity(log0, log)

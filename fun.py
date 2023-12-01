import re
import os
import pandas as pd
import numpy as np
import scipy.stats


def generate_df():
    for i in range(18):
        df = pd.DataFrame()
        # for i in range(1):
        path = 'E://张纪//方老师//17个日志//P' + str(i) + '.txt'
        f = open(path, "r", encoding="UTF-8")
        P = f.readlines()
        f.close()
        result = []
        results1 = []
        for line1 in P:
            # 提取“<trace>”和“</trace>”之间的内容
            re_str = r'string key="concept:name" value='
            m = re.findall(re_str, line1)
            if m:
                results1.append(line1)
        results2 = []
        for line2 in results1:
            j = line2.split('"')
            results2.append(j[3])
        del results2[0:3]
        # print(results2)
        n = 1
        for index in range(1, len(results2)):
            if len(results2[index]) != 1:
                break
            else:
                n = n + 1
        l = len(results2) / n
        for y in range(int(l)):
            temp = []
            for nx in range(n):
                temp.append(results2[nx + y * n])
            result.append(temp)

        case = []
        trace = []
        for s in result:
            case.append(s[0])
            trace.append("".join(s[1:n]))
        df = pd.DataFrame({'caseid': case, 'trace': trace})
        # print(df)
        df1 = pd.DataFrame(df['caseid'].value_counts())
        df1 = df1.rename_axis('index').reset_index()
        df1 = df1.rename(columns={'index': 'caseid', 'caseid': 'frequency'})
        # print(df1)
        df['frequency'] = 0
        for row_a in df.iterrows():
            for row_b in df1.iterrows():
                # print(row_a[1])
                # print(row_b[1])
                if row_a[1]['caseid'] == row_b[1]['caseid']:
                    df.loc[row_a[0], 'frequency'] = row_b[1]['frequency']
                    break
                continue
        df.drop_duplicates('caseid', keep='first', inplace=True)
        df = df.rename_axis('index').reset_index()
        df = df.drop(labels='index', axis=1)
        print('P' + str(i), df)
        df.to_csv('E://张纪//方老师//17个日志//Log_P' + str(i) + '.csv')


def findLength(str_one, str_two):
    """
    str_one 和 str_two 的最长公共子序列
    :param str_one: 字符串1
    :param str_two: 字符串2（正确结果）
    :return: 最长公共子序列的长度
    """
    len_str1 = len(str_one)
    len_str2 = len(str_two)
    # 定义一个列表来保存最长公共子序列的长度，并初始化
    record = [[0 for i in range(len_str2 + 1)] for j in range(len_str1 + 1)]
    for i in range(len_str1):
        for j in range(len_str2):
            if str_one[i] == str_two[j]:
                record[i + 1][j + 1] = record[i][j] + 1
            elif record[i + 1][j] > record[i][j + 1]:
                record[i + 1][j + 1] = record[i + 1][j]
            else:
                record[i + 1][j + 1] = record[i][j + 1]
    return record[-1][-1]


def d_seq(x, y):
    l = findLength(x, y)
    # print(l)
    return 1 - (l / (len(x) + len(y) - l))


def fun_pinghuayingshe(a, b, epsilon=10 ** -7):
    """

    :param a: [[a, b, c]
                [1, 1, 1]]
    :param b:
    :return:
    """
    e = epsilon
    a1 = list(set(b[0]).difference(a[0]))
    b1 = list(set(a[0]).difference(b[0]))
    a2 = list(set(a[0]).union(a1))
    b2 = list(set(b[0]).union(b1))

    p_a = []
    count_r = 0
    count_m = 0
    for i in range(len(a2)):
        if a2[i] in a[0]:
            index = a[0].index(a2[i])
            p_a.append(a[1][index])
            count_m += 1
        else:
            p_a.append(e)
            count_r += 1
    miner = count_r * e / count_m
    for j in range(len(p_a)):
        if p_a[j] != e:
            p_a[j] -= e
    # print(a2)
    # print(p_a)

    p_b = []
    count_r = 0
    count_m = 0
    for i in range(len(b2)):
        if b2[i] in b[0]:
            index = b[0].index(b2[i])
            p_b.append(b[1][index])
            count_m += 1
        else:
            p_b.append(e)
            count_r += 1
    miner = count_r * e / count_m
    for j in range(len(p_b)):
        if p_b[j] != e:
            p_b[j] -= e
    # print(b2)
    # print(p_b)

    b3 = []
    p_b1 = []
    for i in a2:
        index = b2.index(i)
        b3.append(b2[index])
        p_b1.append(p_b[index])
    return [a2, p_a], [b3, p_b1]


def TrMS(l0, l):
    '''

    :param l0:[['AB' 'BD' 'DE' 'EF' 'AD' 'DB' 'BE' 'AC' 'CD' 'DC' 'CE' 'EG']
                ['0.08894827257110136' '0.06890627982439397' '0.1286505058217217'
                '0.12750524909333844' '0.1578545523954953' '0.04886428707768658'
                '0.052490933384233635' '0.07253292613094102' '0.052490933384233635'
                '0.052109181141439205' '0.055735827447986254' '0.0939110517274289']]
    :param l:
    :return:
    '''
    x, y = fun_pinghuayingshe(l0, l, epsilon=10 ** -7)
    # print(x, '\n', y)
    p_x, p_y = np.asarray(x[1]), np.array(y[1])
    M = (p_x + p_y) / 2
    js = 0.5 * scipy.stats.entropy(x[1], M) + 0.5 * scipy.stats.entropy(y[1], M)
    return 1 - js


def SeqAPMS(l0, l):
    '''

    :param l0:
    :param l:
    :return:
    '''
    x, y = fun_pinghuayingshe(l0, l, epsilon=10 ** -7)
    # print(x, '\n', y)
    p_x, p_y = np.asarray(x[1]), np.array(y[1])
    M = (p_x + p_y) / 2
    js = 0.5 * scipy.stats.entropy(x[1], M) + 0.5 * scipy.stats.entropy(y[1], M)
    return 1 - js


def toSAP(l0):
    """

    :param l0: [['ABDEF', 'ADBEF', 'ACDEF', 'ADCEF', 'ADBEG', 'ACDEG', 'ADCEG', 'ABDEG'], [233, 128, 147, 145, 57, 98, 101, 91]]
    :return: [['AB' 'BD' 'DE' 'EF' 'AD' 'DB' 'BE' 'AC' 'CD' 'DC' 'CE' 'EG']
                ['0.08894827257110136' '0.06890627982439397' '0.1286505058217217'
                 '0.12750524909333844' '0.1578545523954953' '0.04886428707768658'
                '0.052490933384233635' '0.07253292613094102' '0.052490933384233635'
                '0.052109181141439205' '0.055735827447986254' '0.0939110517274289']]
    """
    list = []
    p = []
    for i in range(len(l0[0])):
        s = ','.join(l0[0][i])
        s = s.split(",")
        # print(s)

        for j in range(len(s) - 1):
            sap = s[j] + s[j + 1]
            if sap not in list:
                list.append(sap)
                p.append(l0[1][i])
            else:
                index = list.index(sap)
                p[index] += l0[1][i]
        # print([list, p])
    # p = np.array(p)
    # p = p / sum(p)
    return [list, p]


def daoru(l):
    """

    :param l:
    :return:
    """
    l = np.array(l[['trace', 'frequency']])
    l = l.tolist()
    l = list(zip(*l))
    l = [list(l[0]), list(l[1])]
    return l


def pinghuayingshe(log0):
    '''
    将导入的日志转化成迹与其发生的概率分布
    :param log0:
    :return:
    '''
    l0 = np.array(log0[['trace', 'frequency']])
    l0 = l0.tolist()
    l0 = list(zip(*l0))
    l0 = [list(l0[0]), list(l0[1])]
    s0 = sum(l0[1])
    for i in range(len(l0[1])):
        l0[1][i] = l0[1][i] / s0
    # print(l0)
    return l0


if __name__ == '__main__':
    a = [['a', 'b', 'c'], [1, 6, 5]]
    b = [['d', 'e', 'c'], [9, 4, 2]]
    x, y = fun_pinghuayingshe(a, b, epsilon=10 ** -7)
    print(x, '\n', y)

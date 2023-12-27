import pandas as pd
import numpy as np
from collections import defaultdict
import scipy.stats


def trace2trace_frequency(df):
    """
    将df转变成频率迹数组
    :param df:
    :return: [...
            [0.0007097232079489, ['01_HOOFD_010', '01_HOOFD_011', '01_HOOFD_020', '02_DRZ_010', '04_BPT_005', '01_HOOFD_065_0', '01_HOOFD_090', '01_HOOFD_015', '01_HOOFD_030_1', '01_HOOFD_061', '01_HOOFD_030_2', '01_HOOFD_110_0', '01_HOOFD_180', '08_AWB45_005', '01_HOOFD_200', '01_HOOFD_250_0', '01_HOOFD_330', '09_AH_I_010', '01_HOOFD_380', '01_HOOFD_430', '11_AH_II_010', '13_CRD_010', '01_HOOFD_480', '01_HOOFD_490_2', '01_HOOFD_491', '01_HOOFD_490_1', '01_HOOFD_195', '01_HOOFD_375', '01_HOOFD_250_2', '01_HOOFD_490_4', '01_HOOFD_250_1', '01_HOOFD_494a', '01_HOOFD_490_1a', '01_HOOFD_532_0', '01_HOOFD_500', '01_HOOFD_510_0', '01_HOOFD_490_5', '01_HOOFD_510_4', '01_HOOFD_510_1', '01_HOOFD_510_3', '01_HOOFD_495', '01_HOOFD_490_5a', '01_HOOFD_510_2a', '01_HOOFD_515', '01_HOOFD_510_2']]
            [0.0007097232079489, ['01_HOOFD_010', '01_HOOFD_011', '01_HOOFD_020', '02_DRZ_010', '04_BPT_005', '01_HOOFD_065_0', '01_HOOFD_090', '01_HOOFD_030_1', '01_HOOFD_061', '01_HOOFD_015', '01_HOOFD_030_2', '01_HOOFD_110_0', '01_HOOFD_200', '01_HOOFD_250_0', '01_HOOFD_180', '08_AWB45_005', '01_HOOFD_330', '09_AH_I_010', '01_HOOFD_380', '01_HOOFD_430', '11_AH_II_010', '13_CRD_010', '01_HOOFD_480', '01_HOOFD_490_2', '01_HOOFD_110_1', '01_HOOFD_195', '01_HOOFD_250_1', '01_HOOFD_375', '01_HOOFD_490_1', '01_HOOFD_110_2', '01_HOOFD_250_2', '01_HOOFD_490_1a', '01_HOOFD_491', '01_HOOFD_500', '01_HOOFD_532_0', '01_HOOFD_510_0', '01_HOOFD_510_4', '01_HOOFD_495', '01_HOOFD_510_3', '01_HOOFD_494a', '01_HOOFD_515', '01_HOOFD_490_4', '01_HOOFD_510_1', '01_HOOFD_510_2', '01_HOOFD_490_5', '01_HOOFD_490_5a', '01_HOOFD_510_2a']]
            [0.0007097232079489, ['01_HOOFD_010', '02_DRZ_010', '04_BPT_005', '01_HOOFD_065_0', '01_HOOFD_090', '01_HOOFD_011', '01_HOOFD_020', '01_HOOFD_015', '01_HOOFD_061', '01_HOOFD_030_1', '01_HOOFD_030_2', '01_HOOFD_110_0', '01_HOOFD_180', '08_AWB45_005', '01_HOOFD_200', '01_HOOFD_250_0', '01_HOOFD_330', '09_AH_I_010', '01_HOOFD_380', '01_HOOFD_430', '11_AH_II_010', '13_CRD_010', '01_HOOFD_480', '01_HOOFD_490_2', '01_HOOFD_195', '01_HOOFD_250_1', '01_HOOFD_490_1', '01_HOOFD_490_1a', '01_HOOFD_375', '01_HOOFD_250_2', '01_HOOFD_491', '01_HOOFD_500', '01_HOOFD_532_0', '01_HOOFD_510_0', '01_HOOFD_510_2a', '01_HOOFD_490_5a', '01_HOOFD_495', '01_HOOFD_515', '01_HOOFD_494a', '01_HOOFD_510_3', '01_HOOFD_510_1', '01_HOOFD_490_4', '01_HOOFD_510_4', '01_HOOFD_490_5', '01_HOOFD_510_2']]
            ...]
    """
    traces = []
    t = df.values
    for trace in t:
        x = []
        for j in trace:
            if isinstance(j, str):
                x.append(j)
        traces.append(x)
    trace_dict = defaultdict(int)

    # 统计每个迹的出现次数
    for trace in traces:
        trace_dict[tuple(trace)] += 1

    # 计算总迹数
    total_traces = sum(trace_dict.values())

    # 计算频率并转换为小数形式
    trace_freq_list = []
    for trace, freq in trace_dict.items():
        freq_decimal = freq / total_traces
        trace_freq_list.append([freq_decimal, list(trace)])

    return trace_freq_list


def trace_freq_list2list(a):
    fre = []
    tra = []
    for x in range(len(a)):
        fre.append(a[x][0])
        tra.append('->'.join(a[x][1]))
    return [tra, fre]


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


def SeqAPMS(l0, l, e=10 ** -7):
    '''

    :param l0:
    :param l:
    :return:
    '''
    x, y = fun_pinghuayingshe(l0, l, epsilon=e)
    # print(x, '\n', y)
    p_x, p_y = np.asarray(x[1]), np.array(y[1])
    M = (p_x + p_y) / 2
    js = 0.5 * scipy.stats.entropy(x[1], M) + 0.5 * scipy.stats.entropy(y[1], M)
    return 1 - js


if __name__ == '__main__':
    for i in range(1, 6):
        for j in range(1, 6):
            df1 = pd.read_csv("E://张纪//论文//投稿//行为区分//现实事件日志//BPIC2015//BPIC15_" + str(i) + ".csv", index_col=0)
            df2 = pd.read_csv("E://张纪//论文//投稿//行为区分//现实事件日志//BPIC2015//BPIC15_" + str(j) + ".csv", index_col=0)
            a1 = trace2trace_frequency(df1)
            t1 = trace_freq_list2list(a1)
            a2 = trace2trace_frequency(df1)
            t2 = trace_freq_list2list(a1)
            # ax1, ax2 = fun_pinghuayingshe(t1, t2)
            print(str(i)+"and"+str(j))
            print(SeqAPMS(t1, t2, 10 ** -30))

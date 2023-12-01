import os
import pandas as pd
import numpy as np
import scipy.stats
from fun import *
import NDCG


log0 = pd.read_csv('E://张纪//方老师//13个日志//log_无概率//Log_P0.csv', index_col=0)
l0 = pinghuayingshe(log0)
sim = []
LOG = []
for i in range(1, 14):
    # for i in range(1, 3):
    # print('0', '*' * 10, str(i))
    log = pd.read_csv('E://张纪//方老师//13个日志//log_无概率//Log_P' + str(i) + '.csv', index_col=0)
    l = pinghuayingshe(log)
    t = TrMS(l0, l)
    L = 'P' + str(i)
    LOG.append(L)
    sim.append('%.6f' % t)
    # print("%.3f" % t)

answer1 = np.array([LOG, sim]).T
print(answer1)



###########################################################################
# log0 = pd.read_csv('E://张纪//方老师//13个日志//log_有概率//Log_P0.csv', index_col=0)
# l0 = pinghuayingshe(log0)
# sim = []
# LOG = []
# for i in range(1, 14):
#     # for i in range(1, 3):
#     # print('0', '*' * 10, str(i))
#     log = pd.read_csv('E://张纪//方老师//13个日志//log_有概率//Log_P' + str(i) + '.csv', index_col=0)
#     l = pinghuayingshe(log)
#     t = TrMS(l0, l)
#     L = 'P' + str(i)
#     LOG.append(L)
#     sim.append('%.6f' % t)
#     # print("%.3f" % t)
# print(sim)
# answer2 = pd.DataFrame(sim, columns=['sim'],
#                       index=['log01', 'log02', 'log03', 'log04', 'log05', 'log06', 'log07',
#                              'log08', 'log09', 'log10', 'log11', 'log12', 'log13'])
# print(answer2)
#
#
# list = [0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3]
# p = ['log08', 'log02', 'log03', 'log10', 'log12', 'log07', 'log11', 'log01', 'log09', 'log05', 'log04', 'log06', 'log13']
# df = pd.DataFrame([list, p], index=['w', 'log']).T
# df = df.sort_values(by=['log'])
# df = df.reset_index(drop=True)
# print(df)
#
# answer2['weight'] = df['w'].values.tolist()
# print(answer2)
#
# answer2['weight'] = df['w'].values.tolist()
# answer2 = answer2.sort_values(by=['sim'], ascending=False)
# print(answer2)
# list1 = answer2['weight'].values.tolist()
# DCG = NDCG.fun(len(list1), list1)
# IDCG = NDCG.fun(len(list), list)
# print(DCG)
# print(IDCG)
# print(DCG/IDCG)

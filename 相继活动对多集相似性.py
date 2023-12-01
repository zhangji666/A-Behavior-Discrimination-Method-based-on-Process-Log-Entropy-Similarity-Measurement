import os
import pandas as pd
import numpy as np
import scipy.stats
from fun import *
import NDCG

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# log0 = pd.read_csv('E://张纪//方老师//13个日志//log_无概率//Log_P0.csv', index_col=0)
# l0 = daoru(log0)
# l0 = toSAP(l0)
# # print(l0)
# sim = []
# LOG = []
# for i in range(1, 14):
#     # for i in range(1, 3):
#     # print('0', '*' * 10, str(i))
#     log = pd.read_csv('E://张纪//方老师//13个日志//log_无概率//Log_P' + str(i) + '.csv', index_col=0)
#     l = daoru(log)
#     # print(l)
#     l = toSAP(l)
#     Seq = SeqAPMS(l0, l)
#     # L = 'P'+str(i)
#     # LOG.append(L)
#     sim.append('%.3f' % Seq)
#     # print('%.3f' % Seq)
# answer = pd.DataFrame(sim, columns=['sim'], index=['log1', 'log2', 'log3', 'log4', 'log5', 'log6', 'log7', 'log8', 'log9', 'log10', 'log11', 'log12', 'log13'])
# answer = answer.sort_values(by=['sim'], ascending=False)
# # answer = answer.reset_index(drop=True)
# print(answer.T)

################################################################################################
log0 = pd.read_csv('E://张纪//方老师//13个日志//log_有概率//Log_P0.csv', index_col=0)
l0 = daoru(log0)
l0 = toSAP(l0)
# print(l0)
sim = []
LOG = []
for i in range(1, 14):
    # for i in range(1, 3):
    # print('0', '*' * 10, str(i))
    log = pd.read_csv('E://张纪//方老师//13个日志//log_有概率//Log_P' + str(i) + '.csv', index_col=0)
    l = daoru(log)
    # print(l)
    l = toSAP(l)
    Seq = SeqAPMS(l0, l)
    # L = 'P' + str(i)
    # LOG.append(L)
    sim.append('%.3f' % Seq)
    # print('%.3f' % Seq)

answer = pd.DataFrame(sim, columns=['sim'],
                      index=['log01', 'log02', 'log03', 'log04', 'log05', 'log06', 'log07',
                             'log08', 'log09', 'log10', 'log11', 'log12', 'log13'])
# answer = answer.sort_values(by=['sim'], ascending=False)
# answer = answer.reset_index(drop=True)
print(answer)

# list = [0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3]
# p = ['log08', 'log02', 'log03', 'log10', 'log12', 'log07', 'log11', 'log01', 'log09', 'log05', 'log04', 'log06', 'log13']
# df = pd.DataFrame([list, p], index=['w', 'log']).T
# df = df.sort_values(by=['log'])
# df = df.reset_index(drop=True)
# print(df)
#
# answer['weight'] = df['w'].values.tolist()
# answer = answer.sort_values(by=['sim'], ascending=False)
# print(answer)
# list1 = answer['weight'].values.tolist()
# DCG = NDCG.fun(len(list1), list1)
# IDCG = NDCG.fun(len(list), list)
# print(DCG)
# print(IDCG)
# print(DCG/IDCG)

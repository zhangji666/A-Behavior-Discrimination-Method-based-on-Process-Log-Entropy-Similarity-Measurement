from fun import *
import NDCG


def Cross_Entropy(l0, l):
    l_a = np.asarray(l0[1])
    l_b = np.array(l[1])
    # print(l_a, '\n', l_b)
    return -sum(np.nan_to_num(l_a * np.log(l_b) + (1 - l_a) * np.log(1 - l_b)))


log0 = pd.read_csv('E://张纪//方老师//13个日志//log_有概率//Log_P0.csv', index_col=0)
l0 = pinghuayingshe(log0)
CE = []
for i in range(1, 14):
    # for i in range(1, 3):
    # print('0', '*' * 10, str(i))
    log = pd.read_csv('E://张纪//方老师//13个日志//log_有概率//Log_P' + str(i) + '.csv', index_col=0)
    l = pinghuayingshe(log)
    l0_p, l_p = fun_pinghuayingshe(l0, l)
    CE.append(Cross_Entropy(l0_p, l_p))


answer = pd.DataFrame(CE, columns=['CrossEntropy'],
                      index=['log01', 'log02', 'log03', 'log04', 'log05', 'log06', 'log07',
                             'log08', 'log09', 'log10', 'log11', 'log12', 'log13'])
# answer = answer.sort_values(by=['sim'], ascending=False)
# answer = answer.reset_index(drop=True)
print(answer)
answer.to_csv('E:\张纪\方老师//test.csv')

list = [0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3]
p = ['log08', 'log02', 'log03', 'log10', 'log12', 'log07', 'log11', 'log01', 'log09', 'log05', 'log04', 'log06', 'log13']
df = pd.DataFrame([list, p], index=['w', 'log']).T
df = df.sort_values(by=['log'])
df = df.reset_index(drop=True)
print(df)

answer['weight'] = df['w'].values.tolist()
answer = answer.sort_values(by=['CrossEntropy'])
print(answer)
list1 = answer['weight'].values.tolist()
DCG = NDCG.fun(len(list1), list1)
IDCG = NDCG.fun(len(list), list)
print(DCG)
print(IDCG)
print(DCG/IDCG)


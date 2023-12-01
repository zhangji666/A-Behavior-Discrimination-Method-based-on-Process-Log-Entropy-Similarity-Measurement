from math import log
import numpy as np
import pandas as pd


def fun(n, list):
    if len(list) < n:
        print('n大了')
        return 0
    else:
        if n == 1:
            return list[0]
        else:
            return fun(n - 1, list) + (list[n - 1] / log(n, 2))


# def fun(list):
#     sum = list[0]
#     if len(list) == 1:
#         return sum
#     else:
#         for i in range(1, len(list)):
#             sum += list[i]/log(i+1, 2)
#         return sum


if __name__ == '__main__':
    list = [0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3]
    p = ['log08', 'log02', 'log03', 'log10', 'log12', 'log07', 'log11', 'log01', 'log09', 'log05', 'log04', 'log06',
         'log13']
    df = pd.DataFrame([list, p], index=['w', 'log']).T
    df = df.sort_values(by=['log'])
    df = df.reset_index(drop=True)
    print(df)

    list1 = [0.8681999996304512, 0.8674000039696693, 0.7665999993681908, 0.7682000055909157, 0.7783999964594841,
             0.780000002682209, 0.795200003683567, 0.9141999959945679, 0.9095999978482723, 0.8211666662245989,
             0.8328333348035812, 0.7986000016331672, 0.7957999989390373]
    Log = ['log08', 'log02', 'log03', 'log10', 'log12', 'log07', 'log11', 'log01', 'log09', 'log05', 'log04', 'log06',
           'log13']
    answer = pd.DataFrame(list1, index=Log, columns=['sim'])
    print(answer)
    answer['weight'] = df['w'].values.tolist()
    answer = answer.sort_values(by=['sim'], ascending=False)
    print(answer)
    list1 = answer['weight'].values.tolist()
    DCG = fun(len(list1), list1)
    IDCG = fun(len(list), list)
    print(DCG)
    print(IDCG)
    print(DCG / IDCG)

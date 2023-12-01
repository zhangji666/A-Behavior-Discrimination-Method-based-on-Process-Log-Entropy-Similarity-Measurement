import pandas as pd
import numpy as np
import random


def generate_trace0():
    log = ''
    log += 'a'
    probabilities = [0.85, 0.15]
    elements = ['b', 'c']
    result = random.choices(elements, probabilities)[0]
    data = [result, 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace1():
    log = ''
    log += 'a'
    data = ['c', 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace2():
    log = ''
    log += 'a'
    data = ['b', 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace3():
    log = ''
    log += 'a'
    data = ['b', 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'ef'
    return log


def generate_trace4():
    log = ''
    log += 'a'
    data = ['b', 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'eg'
    return log


def generate_trace5():
    log = ''
    log += 'a'
    data = ['c', 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'ef'
    return log


def generate_trace6():
    log = ''
    log += 'a'
    data = ['c', 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'eg'
    return log


def generate_trace7():
    log = ''
    log += 'a'
    probabilities = [0.85, 0.15]
    elements = ['b', 'c']
    result = random.choices(elements, probabilities)[0]
    log += result
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace8():
    log = ''
    log += 'a'
    probabilities = [0.85, 0.05, 0.1]
    elements = ['b', 'c', 'k']
    result = random.choices(elements, probabilities)[0]
    data = [result, 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace9():
    log = ''
    log += 'a'
    probabilities = [0.05, 0.05, 0.9]
    elements = ['b', 'c', 'k']
    result = random.choices(elements, probabilities)[0]
    data = [result, 'd']
    sample_num = 2
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace10():
    log = ''
    log += 'a'
    probabilities = [0.85, 0.15]
    elements = ['b', 'c']
    result = random.choices(elements, probabilities)[0]
    data = [result, 'k', 'd']
    sample_num = 3
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace11():
    log = ''
    log += 'a'
    data = ['b', 'c', 'd']
    sample_num = 3
    temp = random.sample(data, sample_num)
    for i in temp:
        log += i
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace12():
    log = ''
    log += 'a'
    probabilities = [0.85, 0.05, 0.1]
    elements = ['b', 'c', 'd']
    result = random.choices(elements, probabilities)[0]
    log += result
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_trace13():
    log = ''
    log += 'a'
    probabilities = [0.05, 0.05, 0.9]
    elements = ['b', 'c', 'd']
    result = random.choices(elements, probabilities)[0]
    log += result
    log += 'e'
    probabilities = [0.875, 0.125]
    elements = ['f', 'g']
    result = random.choices(elements, probabilities)[0]
    log += result
    return log


def generate_log(x, n):
    LOG = []
    name = 'generate_trace' + str(x)
    generate_t = globals()[name]
    for i in range(1000):
        t = generate_t()
        if t not in LOG:
            LOG.append(t)
    x = [0 for index in range(len(LOG))]
    L = pd.DataFrame(np.array([LOG, x]).T, columns=['trace', 'frequency'])
    L['frequency'] = L['frequency'].astype(np.int64)
    for i in range(n):
        t = generate_t()
        w = L[(L.trace == t)].index.tolist()[0]
        L.loc[w, 'frequency'] += 1
    L = L.sort_values(by=['trace'])
    L = L.reset_index(drop=True)
    L['caseid'] = L.index
    L = L.reindex(columns=['caseid', 'trace', 'frequency'])
    return L


for i in range(14):
    l = generate_log(i, 1000)
    print('Log' + str(i))
    print(l)
    save_path = 'E://张纪//方老师//13个日志//log_有概率//Log_P' + str(i) + '.csv'
    l.to_csv(save_path)

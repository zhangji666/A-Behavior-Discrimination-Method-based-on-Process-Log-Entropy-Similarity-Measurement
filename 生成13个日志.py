import pm4py
import numpy as np
import pandas as pd
from pm4py.algo.simulation.playout.petri_net import algorithm as simulator

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

for i in range(14):
    path = 'E://张纪//方老师//13个日志//p' + str(i) + '.pnml '
    net, im, fm = pm4py.read_pnml(path)
    log = simulator.apply(net, im, variant=simulator.Variants.BASIC_PLAYOUT,
                                    parameters={simulator.Variants.BASIC_PLAYOUT.value.Parameters.NO_TRACES: 1000})
    pm4py.write_xes(log, 'E://张纪//方老师//13个日志//log//log' + str(i) + '.xes ')
    # pm4py.view_petri_net(net, im, fm, format='svg')
    # log = pm4py.play_out(net, im, fm)
    X = []
    for j in log:
        trace = ''
        for j1 in j:
            trace += j1['concept:name']
        # print(trace)
        X.append(trace)
    a = {}
    for j in X:
        if X.count(j) > 1:
            a[j] = X.count(j)
    values = list(a.values())
    keys = list(a.keys())
    l = np.array([keys, values]).T
    l = pd.DataFrame(l, columns=['trace', 'frequency'])
    l = l.sort_values(by=['trace'])
    l = l.reset_index(drop=True)
    l['caseid'] = l.index
    l = l.reindex(columns=['caseid', 'trace', 'frequency'])
    print('Log'+str(i))
    print(l)
    save_path = 'E://张纪//方老师//13个日志//log//Log_P' + str(i) + '.csv'
    l.to_csv(save_path)

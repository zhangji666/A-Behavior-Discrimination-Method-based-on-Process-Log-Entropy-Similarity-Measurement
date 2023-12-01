import pm4py
import numpy as np
import pandas as pd
log = pm4py.read_xes("E://张纪//方老师//17个日志//P17.xes")
X = []
for i in log:
    trace = ''
    for j in i:
        trace += j['concept:name']
    # print(trace)
    X.append(trace)
a = {}
for i in X:
    if X.count(i) > 1:
        a[i] = X.count(i)
values = list(a.values())
keys = list(a.keys())
l = np.array([keys, values]).T
l = pd.DataFrame(l, columns=['trace', 'frequency'])
l['caseid'] = l.index
l = l.reindex(columns=['caseid', 'trace', 'frequency'])
print(l)
sum = 0
f = l['frequency']
for i in f:
    sum += int(i)
print(sum)


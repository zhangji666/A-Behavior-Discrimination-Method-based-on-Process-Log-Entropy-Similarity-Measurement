import pandas as pd
import re

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

for num in range(1, 6):
    # 读取txt文件内容
    with open("E://张纪//论文//投稿//行为区分//现实事件日志//BPIC2015//BPIC15_" + str(num) + ".txt", "r") as file:
        content = file.readlines()

    # 正则表达式匹配活动名称属性值
    pattern = re.compile(r'<string key="concept:name" value="(.*?)"')

    # 提取活动名称并组织成列表
    traces = []
    current_trace = []
    x = 0
    for line in content:
        match = pattern.search(line)
        if match:
            current_trace.append(match.group(1).strip())  # 使用strip去除两端空白字符
        elif line.strip() == '</trace>':
            if x == 0:
                current_trace = current_trace[3:]
                x = 1
            traces.append(current_trace)
            current_trace = []

    # 将 None 替换为空字符串
    # print(traces[0])
    df = pd.DataFrame(traces).replace({None: ''})

    # 删除全为空的列
    df = df.dropna()
    df = df.drop(df.columns[0], axis=1)

    # 显示DataFrame内容
    print(df.head())

    # df.to_csv('E://张纪//论文//投稿//行为区分//现实事件日志//BPIC2015//BPIC15_' + str(num) + '.csv')

import os
import pandas as pd
import numpy as np

# 从sum中移除超时的实例
if __name__ == '__main__':
    root_dir = "/Users/lizhe/Documents/exp/sum"
    res_dir = "/Users/lizhe/Documents/exp/sum_rm"
    solve_time_list = list()
    delete_list = list()
    # pct_files = os.listdir(pct_path)
    # strbit_files = os.listdir(strbit_path)
    # common_files = list(set(pct_files) & set(strbit_files))
    summary_files = sorted(os.listdir(root_dir))

    summary_files.remove('.DS_Store')
    # print(summary_files)
    # for name in summary_files:
    # 通过
    sample = "/Users/lizhe/Documents/exp/sum/zzdubois.csv"

    data = pd.read_csv(sample)
    title_list = data.columns.values.tolist()
    print(title_list)
    print(len(title_list))
    #
    result = pd.DataFrame(columns=title_list)
    # solve time list
    for c in title_list:
        if c.startswith('time'):
            solve_time_list.append(c)

    print(solve_time_list)
    #
    for name in summary_files:
        path = os.path.join(root_dir, name)
        res_path = os.path.join(res_dir, name)
        print(path)
        # name = "/Users/lizhe/Documents/exp/sum/zzdubois.csv"
        #
        data = pd.read_csv(path)
        #     result.append()
        #     # print(data.columns.values.tolist())
        #
        #     print('=====')
        #     print(data)
        #
        for c in solve_time_list:
            data.drop(data[data[c] >= 900].index, inplace=True)
        #
        print(name, data.shape)
        data.to_csv(res_path)

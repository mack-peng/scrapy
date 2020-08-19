# -*- coding: utf-8 -*-
import numpy
import os
import ai_tools
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import  FontProperties

# 解决中文显示问题，仅适用于windows
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决mac中文显示
def get_chinese_font():
    return FontProperties(format='/System/Library/Fonts/PingFang.ttf')


filedata_path = "./bing_count.csv"
output_path = "."

def process_data(data_df):
    data_df.dropna(inplace=True)
    data_df.sort_values(['count'], ascending=False, inplace=True)
    return data_df

def analyze_data(data_df):
    data_df.set_index('name', inplace=True)
    return data_df

def save_plot_results(data_df):
    data_df.to_csv(os.path.join(output_path, 'bing_sort_count.csv'))

    # 柱状图
    data_df.head(20)['count'].plot(kind='bar', title='bing搜索页面数量前20')
    plt.xlabel("关键词")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'bing_search_count.png'))
    plt.show()


def main():
    # 获取数据
    data_df = ai_tools.collect_data(filedata_path)
    ai_tools.inspect_data(data_df)

    # 处理数据(排序)
    data_df = process_data(data_df)

    # 分析数据
    data_df = analyze_data(data_df)

    # 结果展示
    save_plot_results(data_df)
    pass

if __name__ == '__main__':
    main()


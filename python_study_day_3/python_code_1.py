#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-16 13:34:24
# @Author  : longfellow (longfellow.wang@gmail.com)
# @Link    : https://github.com/wadasworths

# 利用python进行数据分析代码第二章

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 利用json规则化
import json

# 读取数据
path = "ch02/usagov_bitly_data2012-03-16-1331923249.txt"
records = [json.loads(line) for line in open(path)]

# print(records[0])
# json模块,把json数据转化成字典类型 records为一个字典类型

# print(records[0]['tz']) = America/New_York
# 对records类的时区统计
# time_zones = [recs['tz'] for recs in records]
# 某些数据记录为空，报错KeyError

time_zones = [recs['tz'] for recs in records if 'tz' in recs]
"""
# 时区列表 time_zones 进行统计
from collections import defaultdict

def get_counts(sequence):
	counts = defaultdict(int)
	for x in sequence:
		counts[x] += 1
	return counts

counts = get_counts(time_zones)
# print(counts['America/New_York']) = 1251
"""
# 对前十个时区进行计数
from collections import Counter

counts = Counter(time_zones)
# counts_common前十时区
counts_common = counts.most_common(10)
# print(counts_common)

from pandas import DataFrame, Series

frame = DataFrame(records)
print(frame['tz'][:10])

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknow'

tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

# 画图

tz_counts[:10].plot(kind='barh', rot=0)
# plt.show()

print(frame['a'][:10])

# 提取浏览器信息
results = Series([x.split()[0] for x in frame.a.dropna()])

print(results[:10])

print(results.value_counts()[:10])

cframe = [frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

# print(operating_system[:5])

by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)

indexer = agg_counts.sum(1).argsort()

count_subset = agg_counts.take(indexer)[-10:]
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
plt.show()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-16 18:43:35
# @Author  : longfellow (longfellow.wang@gmail.com)
# @Link    : https://github.com/wadasworths

# 电影评论统计
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

unames = ['user_id', 'gender', 'age', 'occipation', 'zip']
users = pd.read_table('ch02/movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'moive_id', 'rating', 'timestamp']
ratings = pd.read_table('ch02/movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['moive_id', 'title', 'genres']
movies = pd.read_table('ch02/movielens/movies.dat', sep='::', header=None, names=mnames)

# print(users[:5])
# print(ratings[:5])
# print(movies[:5])

data = pd.merge(pd.merge(ratings, users), movies)

# print(data)

# print(data.ix[0])

mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')

print(mean_ratings[:5])
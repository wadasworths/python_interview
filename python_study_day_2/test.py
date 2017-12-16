# coding=utf-8
# -*- coding=utf-8 -*-
import time

def timer(func):
    def decor(*args):

        start_time = time.time();
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        
        print("run the func use : ", d_time)


    return decor;

@timer  #printSth = timer(printSth) -> printSth = decor
def printSth(str, count):
    for i in range(count):
        print("%d hello,%s!"%(i,str))



printSth("world", 100)
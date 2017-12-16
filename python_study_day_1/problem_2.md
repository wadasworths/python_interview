# @Date    : 2017-12-13 19:58:50
# @Author  : longfellow (longfellow.wang@gmail.com)
# @Link    : https://github.com/wadasworths
# @Version : python_interview

1.python函数中的参数传递：

python中类型是属于对象的，不是属于变量的，所有变量都可以看成是"内存中对象的一个引用"。
对象有两种，可更改的（mutable）{string,tuples,numbers}
不可更改的（imutable）{list,dict,set}

2.list,tuples,dict和set之间的区别：

list（列表），本质上是一个可变的有序表，类似于数组，list_a = [1, 2, 3, 4]
tuples（元组）,类似于list，不可更改的有序表，tuples_b = (1, 2, 3, 4) 
[!注意：tuple的标志是‘,’ 例如： a, b = b, a 这种赋值]，定义只有一个元素的tuples_b = (1,)而不是tuples_b =(1)
dict，字典，类似于关联数组，dict_c = {'index':'value', 'one':'first'}
set，类似于dict，一组key的集合，但是不存储value，（set中没有重复的key）
s = set([1, 2, 3])

s = set([1, 1, 2, 2, 2, 3])  s = {1, 2, 3}   利用set，可以去除重复的元素。

teststring = 'aabbbccccdddd'  set(teststring) = {'a', 'b', 'c', 'd'} 
list(set(teststring)) = ['b', 'd', 'c', 'a'](注意：顺序)   
str = list(set(teststring))
list.sort(str) = ['a', 'b', 'c', 'd']

3.python中的单下划线，双下划线
_foo, 用来指定私有变量
__foo__, Python内部的名字,用来区别其他用户自定义的命名,以防冲突 例如有__new__  __init__
__foo, 解析器用_classname__foo来代替，以区别和其他类相同的命名,它无法直接像公有成员一样随便访问,通过
targetname._classname__foo这样的方式可以访问_

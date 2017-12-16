12.range和xrange的区别：

xrange是python3中出现的写法，在《python高性能编程》一书中
```
# 实现range

def range(start, end, step=1):
	sequence = []
	if start < end:
		sequence.append(start)
		start += step
	return sequence

# 实现xrange
def xrange(start, end, step=1):
	if start < end:
		sequence += start
		start += step
	yeild sequence
```

xrange实现是利用生成器，而range是利用迭代器，对于内存的性能xrange更为好

13.read, readline, readlines的方式区别

read是读取整个文件
readline读取下一行，使用的是生成器的方法
readlines按行读取，使用的是迭代器

思考，对于很大的文件，一般来说使用readline，内存可能不够。

14.is和==

is是对比两个变量的地址，==是对比值

15.python里的copy和deepcopy

```
import copy

a = [1, 2, 3, 4, ['a', 'b']]

b = a #赋值，传递对象的引用
c = copy.copy(a) ##对象拷贝，浅拷贝
d = copy.deepcopy(a) #对象拷贝，深拷贝
```

16.python函数式编程：

filter,map,reduce之前的关系：

filter函数的功能相当于过滤器，调用一个布尔函数```bool_func```来迭代遍历每个seq中的元素。返回一个使bool_seq为true的元素的序列。
```
a = [1,2,3,4,5,6,7]
b = filter(lamda x: x>5, a )
print(b) = [6,7]
```

map是对seq的每一个元素进行函数操作
```
c = map(lamda x: x*x, [1,2,3])
print(c) = [1,4,9]
```

reduce是对seq的每一个元素迭代调用函数
```
reduce(lamda x,y:x*y, range(1,4))
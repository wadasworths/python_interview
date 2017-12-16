# @Date    : 2017-12-14 12:46:46
# @Author  : longfellow (longfellow.wang@gmail.com)
# @Link    : https://github.com/wadasworths
# @Version : iterators and generators

4.列表生成式&&字典生成式

```
[x*x for x in range(1,11) ] = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[x*x for x in range(1,11) if x % 2 == 0] = [4, 16, 36, 64, 100]

# 字典生成式
dic = {key: value for key, value in iterable}

org_dict = {'x': 1, 'y': 2, 'z': 3}
new_dict = {v: k for k,v in enumerate(org_dict)}
```

5.迭代器和生成器

关键词```yield```

将列表生成式中[]改成() 之后数据结构是否改变？
```
L = [x*x for x in range(10)] = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

 L = (x*x for x in range(1,11)) = <generator object <genexpr> at 0x000001B679AE4BF8>
 ```

 通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
 在Python中，我们可以采用生成器：边循环，边计算的机制—>generator

```
myiterators = [x*x for x in range(1,4)]
for i in myiterators:
	print(i)

>>1
>>4
>>9
>>myiterators = [1, 4, 9]

mygenerators = (x*x for x in range(1,4))
for i in mygenerators:
	print(i)

>>9
>>9
>>9
>>mygenerators = 9

# 再次执行
for i in mygenerators:
	print(i)
# 什么也不输出
```

生成器和迭代器的区别就是用()代替[],还有你不能用for i in mygenerator第二次调用生成器:首先计算1,然后会在内存里丢掉1去计算4,直到计算完9.、

关键字```yeild```类似于```return```,返回一个生成器。

6.r'', u'', b'', f''之间的区别：
u'unicode'  构造出来的是unicode, 否则的话是string类型
r'' 原生字符

7.常见的linux系统调用：

fork, copy, clone, kill, getpid, exit, 

8.生成器：
面试题，写一个生成器来输出函数的执行时间。

```
import time 

def func_time(func):
	def func_inner():
		start_time = time.time()
		func(*args)
		end_time = time.time()
		run_time = end_time - start_time
		print(run_time)
	return func_inner
````

9.装饰器中wraps的作用：

python装饰器(decorators)在实现的时候，被装饰的函数实际上已经编程另外一个函数，为了不影响使用，python中```functools```包中提供了一个叫```wraps```的装饰器来消除这样的副作用。

个人理解：加了装饰器之后，已经变成另外一个函数（内联函数，例如上例中：func_inner函数）```wraps```用来消除这种副作用、

上述函数的改写：

```
from functools import wraps
import time 

def func_time(func):
	@wraps(func)
	def func_inner(*args, **kwargs):
		start_time = time.time()
		func(*args)
		end_time = time.time()
		run_time = end_time - start_time 
		print(run_time)
	return func_inner
```
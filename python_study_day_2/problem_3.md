# @Date    : 2017-12-14 12:46:46
# @Author  : longfellow (longfellow.wang@gmail.com)
# @Link    : https://github.com/wadasworths
# @Version : binarg_search

10. 二分查找

```
def binary_search(target, nums):
	min, max = 0, len(nums)
	while True:
	if min >= max:
		return -1
	mid = (min + max) // 2
	if nums[mid] > target:
		max = mid
	elif nums[mid] < target:
		min = mid + 1
	else:
		return mid
```

11.二分查找的优化实现：```bisect模块```

```
import bisect 
import random

def binary_search(nums, target):
	"""binsect_left 返回第一个比target大的值的下标
	i = bisect.bisect_left(nums, target)
	if i ==len(nums):
		return i -1
	elif nums[i] == target:
		return i
	elif i > 0:
		j = i - 1
		if nums[i] - target > target - nums[i]
		return j
	return i
```

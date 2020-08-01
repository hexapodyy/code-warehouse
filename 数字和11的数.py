'''
date:2020-8-1
问题：在任意连续n个正整数中，一定有一个数，其数字和是11的倍数。求n的最小值。
'''


# 函数作用：求参数n的数字和
def sumnumber(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum


# 收集范围内所有数字和为11的倍数的正整数，存入list1
fanwei = 10**8
list1 = []
for i in range(fanwei):
    if sumnumber(i) % 11 == 0:
        list1.append(i)
print(len(list1))

# 依次计算list1中相邻元素的差，存入list2.
# flag为最大值的位置
list2 = []
for i in range(len(list1) - 1):
    list2.append(list1[i + 1] - list1[i])
flag = list2.index(max(list2))
print(len(list2))

# 输出结果，为1000019-999980=39
a = list1[flag + 1]
b = list1[flag]
print("%d - %d is %d" % (a, b, a - b))

'''结果：
9090909
9090908
1000019 - 999980 is 39'''

# list3为差最大的前10名，结果发现都是29
'''list3 = sorted(list2, reverse=True)
for j in range(10):
    print(list3[j], end=' ')
'''
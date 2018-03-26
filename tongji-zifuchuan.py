#encoding:utf-8
__author__ = 'zhouxuan-s'
import os
import string
'''
统计指定字符在txt出现的个数
'''
os.chdir('E:/PycharmProjects/py-lianxi') #改变当前目录，到指定目录中
f=open('account.txt')
s=f.read()
print(s.count('a'))
f.close()


'''
统计txt中出现频率最高的字符串
'''
os.chdir('E:/PycharmProjects/py-lianxi') #改变当前目录，到指定目录中
f=open('account.txt')
s=f.read()
#把字符串分割成单个单词列表
list1=s.split()
print(list1)

#把列表转为集合，为了去除重复项
set1=set(list1)
print(set1)

#把集合转换成列表，集合元素没有顺序，没有索引属性，而列表有
list2=list(set1)
print(list2)

#创建一个空的字典
dir1={}
for x in range(len(list2)):
    dir1[list2[x]]=0
    for y in range(len(list1)):
        if list2[x]==list1[y]:
            dir1[list2[x]]+=1

print(dir1)

#输出字典中值最大key对应的键，txt中频率最高的字符串
print(sorted(dir1,key=lambda x:dir1[x])[-1])

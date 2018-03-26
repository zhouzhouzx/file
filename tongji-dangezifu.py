#encoding:utf-8
__author__ = 'zhouxuan-s'
import os
import string
"""统计单个字符或字符串出现的次数：
print(ss_str.lower().count('e'))
lower将大写变成小写，统计的时候会将大写和小写都统计
"""

'''
统计一个文档中，各个字符出现的次数
'''
os.chdir('E:/PycharmProjects/py-lianxi')
f=open('account.txt', 'r+')
s=f.read()
s1=s.replace('\n','') #按行读取文件并去掉换行
print("s1:"+s1)
s2=s.replace(' ','') .replace('\n','')  #删除字符串之间的空格和换行符

f.seek(0)  #将偏移量置0
f.truncate()  #清空文件
f.write(s2)   #写文件
print(s2)
list1=list(s2)
print(list1)

set1=set(list1)
list2=list(set1)
dr={}
for x in range(len(list2)):
    dr[list2[x]]=0
    for y in range(len(list1)):
        if list2[x]== list1[y]:
            dr[list2[x]] +=1
print(dr)


'''
统计txt中出现频率最高的字符，并打印其个数
'''
print(sorted(dr,key=lambda x:dr[x])[-1])


#下周写读一行，写一行，不是一次性全读

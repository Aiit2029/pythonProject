"""
md5加密算法：属于hashlib
MD5 算法具有确定性，即只要输入内容相同，无论何时何地进行计算，生成的 MD5 值都是固定且唯一的。
"""
import hashlib
# 获取一个加密对象
m = hashlib.md5()
# 使用加密对象的update方法进行加密
m.update(b'hello')
m.update(b'world')
# 通过hexdigest方法 获取加密的结果

res =m.hexdigest()
print(res)

result = hashlib.md5(b'114276003.wegame').hexdigest()
print(result)

'''
两个方法一样，可以不使用update 但是m.update可以多次调用
如果内容有中文可以使用字符串的  .encode('utf-8') 来转换
如果不使用 .encode('utf-8') 可以使用 (b'')直接表示本字符串将 转化成二进制
'''
# ret = hashlib.md5('中国人'.encode('utf-8')).hexdigest()
# print(ret)

# ret = hashlib.md5(b'123456').hexdigest()
# print(ret)
# print(len(ret))

# e10adc3949ba59abbe56e057f20f883e
# e10adc3949ba59abbe56e057f20f883e


#   JavaScript Object Noptation
#   :  脚本兑现标记语言
#  简单的数据交换格式

##  序列化  ：线性  与  结构化  之间的转化内叫做序列化和反序列化
# serialization  和 deserialization

# 什么是线性 :  流式数据  (磁盘上的文件)，数据之间没有引用关系

# 什么是结构化 :  有所引用  有一堆的方法和属性

import json

##  json.dumps()  转换成字符串   序列化到内存中
# json.dumps([1,2,3])  变成了字符串
#  json.dumps(obj)

## json.dump   将内容转换成字符串 然后传入文件中    序列化到文件中
#  json.dump([1,2,3],filename)
# json.dump(obj,filename)

## json.loads()   转换成对应形式的 数据类型，除了set  反序列化到内存中
# res = '[1,2,3]'
# json.loads(res)  转换成列表了
# json.loads(obj)

## json.load  从文件中反序列化出来内容
# json.load(filename)

# json 文件通常一次性写，一次性读

# 使用另一种方式可以实现多次写，多次读
# 把需要序列化的对象 ，通过多次序列化的方式，用文件的write方法 ，吧多次序列化后的json字符串写到文件中
with open('json_demo.json', 'w+', encoding='utf-8') as f:
    f.write(json.dumps([1, 2, 3, 4, 5] + '\n', ensure_ascii=False))
    f.write(json.dumps([6, 7, 8, 9, 1] + '\n', ensure_ascii=False))

# 把分词序列化的json字符串 ，反序列化回来
with open('json_demo.json', 'r+', encoding='utf-8') as f:
    # res = json.loads(f.readline().strip())
    # res2 = json.loads(f.readline().strip())
    for i in f:
        print(json.loads(i.strip()))

# 单位
#  t -> text
#  b -> binary  二进制
# 方式
#  a -> append
#  w -> write
#  r -> read）

#  元组一旦被序列化  就会变成列表
# with open('json_demo.json', 'w+',encoding='utf-8') as f:
#     s = json.dumps([1,2,3])
#     f.write(s)
#
#     print(s)
#     print(type(s))

# 从文件中开始反序列化

with open('json_demo.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
    print(type(res))
    print(res)

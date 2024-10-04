# import sys
# request_info = sys.argv[1]
# operator_x = sys.argv[2]
# n = sys.argv[3]
#
#
# f = open("stock_data.txt",'r',encoding='utf-8')
# list_data = []
# for line in f:
#     line = line.strip().split(',')
#     list_data.append(line)
# while True:
#     print("股票查询接口>>")
#     for i in list_data[0]:
#         for j in list_data[1:]:
#             if request_info == i and operator_x == '>':
#                 eval(f'{list_data[j][list_data.index(i)]}>{n}')
#             elif request_info == i and operator_x == '<':
#                 eval(f'{list_data[j][list_data.index(i)]}<{n}')


import sys

def process_stock_data(**kwargs):
    # 打开文件并读取数据
    with open("stock_data.txt", "r",encoding='utf-8') as f:
        lines = f.readlines()

    # 提取列名和数据行
    headers = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]

    # 根据请求信息和操作符筛选数据
    results = []
    for row in data:
        if request_info in headers and row[headers.index(request_info)]:
            value = float(row[headers.index(request_info)])
            if operator_x == '>' and value > n:
                results.append(row)
            elif operator_x == '<' and value < n:
                results.append(row)

    # 打印结果
    for result in results:
        print(result)

if __name__ == "__main__":
    # 从命令行获取参数
    request_info = input("请输入要要查询的股票")
    operator_x = input("请输入计算符号")
    n = int(input("请输入数字"))
    # 处理股票数据
    process_stock_data(request_info, operator_x, n)
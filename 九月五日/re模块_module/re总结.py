# '''
#
# 123
# '''
#
# '''
#
#
# '''
#
import re
#
# #  re.split
#
# # ret = re.split(r'\d+','1as23asd3asd21asdadasd')
# # ret = re.split(r'(\d)\d','1as23asd3asd21asdadasd')
# # print(ret)
#
# # re.sub   可以指定  替换多少次
#
# # ret = re.sub(r'\d+','H','1as23asd3asd21asdadasd',1)
# # print(ret)
#
#
# # re.subn  替换结束之后会 告诉你替换了多少次
#
# #('HasHasdHasdHasdadasd', 4)
# # ret = re.subn(r'\d+','H','1as23asd3asd21asdadasd')
# # print(ret)
#
#
exp = '1 - 2 * ((60-30 + (-40/5) * (9-2*5/3 + 7 / 3*99/4*2998 + 10 *568/14)) - (-4*3)/(16-3*2))'
ret = re.findall(r'\([^()]\)', exp)
# print(s)
# # 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# ret = re.findall('([+-]?\d+|[+\-*/()])',s)
print(ret)
#
#
#
#
#
#


# import re
#
# exp = '1 - 2 * ((60-30 + (-40/5) * (9-2*5/3 + 7 / 3*99/4*2998 + 10 *568/14)) - (-4*3)/(16-3*2))'
#
# # 定义正则表达式匹配数字和运算符的组合
# pattern = re.compile(r'([-+]?\d+(?:\.\d+)?|[+\-*/()])')
#
# # 使用正则表达式找到所有匹配项
# elements = pattern.findall(exp)
#
# # 定义一个栈来进行计算
# stack = []
#
# for element in elements:
#     if element.isdigit() or '.' in element:
#         # 如果是数字，直接入栈
#         stack.append(float(element))
#     else:
#         # 如果是运算符
#         if element == '+':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             stack.append(num1 + num2)
#         elif element == '-':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             stack.append(num1 - num2)
#         elif element == '*':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             stack.append(num1 * num2)
#         elif element == '/':
#             num2 = stack.pop()
#             num1 = stack.pop()
#             if num2!= 0:
#                 stack.append(num1 / num2)
#             else:
#                 raise ValueError("Division by zero")
#
# # 最终栈中剩下的结果就是计算结果
# result = stack[0]
#
# print(result)
# #

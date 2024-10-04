# 记忆元字符

'''
\d:  匹配 所有数字
\D:  匹配所有非数字

\W: 匹配  非数字字母下划线
\w: 匹配  数字字母下划线

\S  匹配  非空格
\s: 匹配  空格
{n} 匹配n次
{n,}至少匹配n次
{n,m} 匹配n到m次

[^123]  匹配非123的字符
()分组 匹配  (123|4556) 匹配 123 或 4556

.  代表除了换行符以外的所有字符
*  表示匹配 0 到 无数次
+  表示匹配 1 到 无数次
?  表示匹配 0 或  1 次
'''
'''
贪婪匹配:  会按照尽量多的情况下匹配

回溯算法
\d{3,}6 
先进行 \d{3,} 
然后从结尾 往回找  6


非贪婪匹配


'''














# mysql 中设置 自动增长 ，需要 这个值 为一个key， 才能设置自动增长

# show databases
# show tables
# create database
# create table

# alter  通常用来改变  表的 基本结构 字段的 设置
# update 通常用来改变  表中某行数据 或者某个数据 的内容

# alter

# alter table t1 modify name char(3);
# alter table t1 change name name1 char(2);
# 什么时候用 modify  什么时候用change
# 当只修改字段的 大小，类型时  使用modify

# 当 要修改字段的 名称和类型大小时 可以使用change

# 事务
# 当开始事务时 ，将 事务中的 多次操作 当作 一次 原子性操作 使用，
# 如果 所有操作 全部完成 ，这次原子性操作 则完成
# 如果 中途有一步 出现问题，未完成， 则 所有操作全部回滚 到未执行 时

# 插入多条数据
# insert into table1 values(1,'刘XX'),(2,'劉智迪');
# 插入 指定的字段 中数据
# insert into table1(name) values('刘桑')


# 查看表结构
# desc table1  (describe)
# 只能看到 部分的约束条件内容，看不到编码方式，引擎

# show create table table1
# 可以看到所有的 内容， 通过 创建表的sql语句的形式 给出
# 例如 :
'''
CREATE TABLE `table_name1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(18) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8
'''


# delete from table1
# 如果自增的id ，在删除之后 这个id 仍然会根据删除前的id 继续自增，而不是从零开始

# truncate table1
# 数据量大 用这个， 删除的速度快， 而且自增的id 直接从零开始

# 内连接 ：  inner join
# select table1.id ,table1.sex,table2.name from table1 inner join table2 on table1.dept_id = table2.id;
# 相当于
# select table1.id ,table1.sex,table2.name from table1,table2 where table1.dept_id = table2.id;

# 左外连接 ：
# 两表相连， 优先显示 左表 所有内容， 左表有，而右表没有的部分用 null 代替
# select table1.id ,table1.sex,table2.name from table1 left join table2 on table1.dept_id = table2.id;

# 右外连接
# 两表相连， 优先显示 右表 所有内容， 右表有，而左表没有的部分用 null 代替

# 全外连接 full join
# mysql 不支持 full join
# 使用 左外连接 union 右外连接 代替
# union 会 剔除 重复的部分
# 而 union all  不会




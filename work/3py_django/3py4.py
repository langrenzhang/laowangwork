"""
#coding=utf-8

'''

create table 'form3' (
    `id` integer PRIMARY KEY autoincrement,
    `title` varchar(255) not null,

    );



id name  age tall
1  李磊   18  175   
 2   小美    18   162
 3    李磊  17   175




1.为请求指定一个路由 route.py
2.路由绑定方法，写一个方法
3.从数据库里拿到数据
4.渲染模板




1.从数据库里拿出数据
2.放入python的数据结构 dict list
3.操作这些数据
4.渲染数据


django开发之 web扫盲课

数据库：
    1.关系型数据库 mssql mysql sqlite   sql 
    2.nosql数据库 mongodb 

    sql 操作 关系型数据库 的 结构化查询语言


码农数据库操作三部曲：

    1.建立数据库 （既然他是关系型的，是有关系的，那我们得先确定关系。）
    关键词 create table
    确定非空，默认等熟悉  not null , default ''
    自增id： 保证唯一值


    2.建立索引 
    为什么要建立索引？ 尽可能避免遍历。
    其他常用索引  1.自增 2.唯一  unique

    3.添删改查
    insert 添加
    update 更新
    delete 删除
    select 查询

码农如何理解数据库的结构：

database -> table -> col
数据库   -》 数据表 -》 列


0.create table 'form3' (`id` integer PRIMARY KEY autoincrement,`title` varchar(255) not null);
1.insert into table (col1) values (value2)
2.update table  set col1 = new_value1 where col1 = value1
3.delete from table where col1 = value1
4.select col from table where col = value1




insert into  table (col1) values (value2)


update table  set col1 = new_value1 where col1 = value1


update table

set  （这里跟修改）

where （这里跟具体的查询条件）




delete from table

where 



'''


"""
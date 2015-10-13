"""
#coding=utf-8


'''
model来了

ror


sql "select * from sth where a = 4"
orm  db.sth.where({'a':4}).find()
mysql postgres sqlite

小概念快速入门：
	1.model让程序员基本不用写sql。
	2.model将表结构映射到对象。
	3.orm可以操作这些对象。
	4.crud 增加(Create)、查询(Retrieve)（重新得到数据）、更新(Update)和删除(Delete)
	5.model和orm都是黑箱子。所以，程序员不可以不会sql。
	6.它可以兼容一些数据库后端。


model的建立


	我们可以这样写sql:

	CREATE TABLE "article" (
	    "id" serial NOT NULL PRIMARY KEY,
	    "title" varchar(30) NOT NULL,
	    "content" text NOT NULL,
	);


	我们这样写model:

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
	    
	    
生成途径：
	1.修改settings.py installed_apps 
	2.定义好数据库路径
	3.执行 manage.py syncdb


看看生成sql：
	python manage.py sqlall article

今天的作业：
 	python manage.py shell
 	用shell写点数据进去吧。

'''



django-admin startapp article



"""
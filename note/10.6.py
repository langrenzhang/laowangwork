"""

沙盒环境：
安装virtualen环境
1 sudo apt-get install python-virtualenv 
创建沙盒 导入变量
2 virtualenv /home/zhangshuo/virtual/
进入沙盒 启动虚拟环境
3 source ~/virtual/bin/activate
3 . ~/virtual/bin/activate


虚拟主机
host:  /etc/hosts
127.0.0.1  e.com


"""


"""
通过命令：sudo apt-get install python-virtualenv或者 sudo pip install virtualenv

然后建立一个测试目录：

mkdir testvirtual

cd testvirtual

然后创建一个虚拟环境：virtualenv env1

cd切换到该目录下，执行命令：source bin/activate

你会发现在shell提示符前面多了(env1)这个提示，这就说明你已经是在虚拟环境中，在这个里面你可以安装任意的python库，而不用担心会把系统自带的python库搞乱。

另外有一个工具，封装了创建虚拟环境的过程，不需要再使用source ［路径］来创建，只需使用一个命令，不需考虑路径。

这个额外的工具就是：virtualenvwrapper。[感谢@koonkai指正]

通过 pip install virtualenvwrapper 安装。

安装完成之后，需要在用户根目录下（即/home/[username]）的.bashrc末尾加入：
source /usr/local/bin/virtualenvwrapper.sh

有的人写是在.bash_profile文件中加入，不过我测试没有成功。

设置好之后，你就可以通过下面的命令来操作虚拟环境了：

创建并进入环境：mkvirtualenv env1
退出环境：deactivate
进入已存在的环境或者切换环境：workon env1或者env2
删除环境： rmvirtualenv env1

"""
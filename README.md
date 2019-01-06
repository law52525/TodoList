
# TodoList

### 起因

[show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)

#### Python 练习册，每天一个小程序

第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。



### 使用

我的Python版本

```bash
python --version
Python 3.6.4
```

##### 第一步 环境

###### 创建虚拟环境：
`python -m venv venv`

###### 激活虚拟环境：
在 Windows 下：
`venv\Scripts\activate`
类Unix系统下：
`. venv/bin/activate`

######安装依赖：

`pip install -r requirements.txt`

##### 第二步 数据库配置

######创建task模型：

`python manage.py makemigrations todo`

######在数据库里创建自定义的模型的数据表：

`python manage.py migrate`

##### 第三步 创建账号

```bash
python manage.py createsuperuser
用户名 (leave blank to use 'mayi'):
电子邮件地址:
Password:
Password (again):
Superuser created successfully.
```

##### 第四步 启动服务

```bash
python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
January 06, 2019 - 18:32:25
Django version 2.1.5, using settings 'TodoList.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```



访问http://127.0.0.1:8000/

![](https://i.imgur.com/G70mG2n.png)
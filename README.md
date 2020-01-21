# django的一些例子

## 部署启动项目

```bash
$git clone https://github.com/yunqingqing/django_practice.git
$cd django_practice
$sudo docker-compose  up
```

目前是apache+mod_wsgi启动服务, 服务地址: http://127.0.0.1

## 初始化做的一些事

```bash
django-admin startproject django_practice
pip freeze > ./requirements.txt
```

## 国际化

在`SessionMiddleware`后增加`django.middleware.locale.LocaleMiddleware`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LANGUAGES = [
  ('en', 'English'),
  ('zh-cn', 'Chinese'),
]

LOCALE_PATHS = [
    './locale'
]

```

先在 项目 目录下创建 locale 目录
服务端模板使用翻译加上这个tag `{% load i18n %}`
收集翻译字符串 `django-admin makemessages -l zh_CN`
编译翻译文件   `django-admin.py compilemessages`

注意：如果是新起了一个线程，那个线程里的翻译会使用`settings.LANGUAGE_CODE`设置的语言

## mysql连接池

核心代码: `django_practice/utils/sql_pool/base.py`
使用了`sqlalchemy`提供的连接池模块
sqlalchemy的一些配置,目前是硬编码的,可以抽出到django的配置中

```python
SQLALCHEMY_QUEUEPOOL = {
    'pool_size': 100,
    'max_overflow': 10,
    'timeout': 5,
    'recycle': 119,
```

配置`settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'utils.sql_pool',
        'NAME': 'dj',
        'HOST': '127.0.0.1',
        'PASSWORD': '123456',
        'USER': 'root'
    }
}
```

benchmark:  `ab -n 10000 -c 100 http://127.0.0.1/users/`, 使用连接池后RPS有了显著的提升

不使用连接池
```
Server Software:        Apache/2.4.38
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /users/
Document Length:        146 bytes

Concurrency Level:      100
Time taken for tests:   50.743 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      4720000 bytes
HTML transferred:       1460000 bytes
Requests per second:    197.07 [#/sec] (mean)
Time per request:       507.433 [ms] (mean)
Time per request:       5.074 [ms] (mean, across all concurrent requests)
Transfer rate:          90.84 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       5
Processing:   307  506 749.4    421    8275
Waiting:      297  486 748.1    401    8242
Total:        308  506 749.6    421    8277

Percentage of the requests served within a certain time (ms)
  50%    421
  66%    444
  75%    460
  80%    471
  90%    510
  95%    549
  98%    640
  99%   7707
 100%   8277 (longest request)

```

使用了连接池, 连接池大小10

```
Server Software:        Apache/2.4.38
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /users/
Document Length:        146 bytes

Concurrency Level:      100
Time taken for tests:   34.374 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      4720000 bytes
HTML transferred:       1460000 bytes
Requests per second:    290.92 [#/sec] (mean)
Time per request:       343.742 [ms] (mean)
Time per request:       3.437 [ms] (mean, across all concurrent requests)
Transfer rate:          134.09 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       5
Processing:   178  342 405.2    299    4561
Waiting:      171  317 405.0    274    4515
Total:        178  343 405.5    299    4564

Percentage of the requests served within a certain time (ms)
  50%    299
  66%    313
  75%    323
  80%    329
  90%    347
  95%    366
  98%    396
  99%   4159
 100%   4564 (longest request)
```
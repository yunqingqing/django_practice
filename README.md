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

benchmark: 相同条件下,使用过了连接池在100并发下,可以比不使用连接池多50左右的RPS
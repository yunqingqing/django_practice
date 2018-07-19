
## 初始化做的一些事
```
django-admin startproject django_practice
pip freeze > ./requirements.txt
```

## 国际化

在`SessionMiddleware`后增加`django.middleware.locale.LocaleMiddleware`
```
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
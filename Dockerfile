FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /webapps
WORKDIR /webapps

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

# apache + mod_wsgi
RUN apt-get install -y apt-utils apache2 apache2-utils
RUN apt-get -y install libapache2-mod-wsgi-py3
ADD ./httpd/django-practice-vhost.conf /etc/apache2/sites-available/000-default.conf

# python相关
RUN pip install -U pip setuptools
COPY requirements.txt /webapps/
RUN mkdir $HOME/.pip/
RUN echo "[global]" > $HOME/.pip/pip.conf
RUN echo "trusted-host =  mirrors.aliyun.com" >> $HOME/.pip/pip.conf
RUN echo "index-url = https://mirrors.aliyun.com/pypi/simple" >> $HOME/.pip/pip.conf
RUN pip install -r /webapps/requirements.txt

# mysql驱动问题修复
RUN sed -i "s/version < (1, 3, 13)/version < (0, 0, 0)/g" /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/base.py

ADD . /webapps/

# Django service
CMD ["python", "/webapps/manage.py", "migrate"]
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
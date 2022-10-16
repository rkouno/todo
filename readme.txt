==============初回導入作業==============
--仮想環境の作成--
$ mkdir djangogirls
$ cd djangogirls
$ python -m venv myvenv
--仮想環境の起動--
$ myvenv\Scripts\activate
--Djangoのインストール--
~$ python -m pip install --upgrade pip
~$ echo Django~=3.2.10 > requirements.txt
~$ pip install -r requirements.txt
--プロジェクト作成--
~$ django-admin startproject config .
-- change source code setting.py--
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
--DB 作成--
~$ python manage.py migrate
========================================
===============デプロイ=-------==========
$ git init
$ git config --global user.name rkouno
$ git config --global user.email rkouno@odp.co.jp
$ git status
$ git add --all .
$ git commit -m "app, first commit"
$ git remote add origin https://github.com/rkouno/todo.git
$ git push -u origin master
--pythonanywhere--
$ pip3.7 install --user pythonanywhere
$ pip3.7 install --user pythonanywhere https://github.com/rkouno/todoapps.git
$ pa_autoconfigure_django.py --python=3.10 
--再インストール--
pa_autoconfigure_django.py --nuke --python=3.6 https://github.com/rkouno/todo.git
========================================
===========アプリケーション作成===========
--アプリケーション作成--
~$ python manage.py startapp anime
--setting.py INSTALLED_APPS add--
'anime.apps.AnimeConfig',
--create table--
python manage.py makemigrations book
python manage.py migrate book
========================================
===========追加インストール===========
pip install requests
pip install beautifulsoup4
========================================

===========静的ファイルの読み込み===========
$ workon rkouno.pythonanywhere.com
(ola.pythonanywhere.com)$ python manage.py collectstatic
========================================
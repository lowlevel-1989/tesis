========================
Biblioteca API
========================

Working Environment
===================


Virtualenv with virtualenvwrapper
---------------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you::

    $ mkdir biblioteca
    $ mkvirtualenv -a biblioteca biblioteca-dev


Installation of Dependencies
-----------------------------
Make sure you install the packages required for all pip dependencies to work properly::

    $ sudo aptitude install python-dev python-pip libpq-dev

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements/production.txt


Setup for development
-----------------------

For the local database setup, 
then run::

    python manage.py syncdb

Now import the recommendeds

    python manage.py loaddata dewey/fixtures/data_dewey.json


Finally, start the local server::

    python manage.py runserver
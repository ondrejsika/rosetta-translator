Rosetta translator
==================

Django project with rosetta configured as translator only.

* __Authors__: [Ondrej Sika](http://ondrejsika.com/c.html)
* __GitHub__: <http://github.com/ondrejsika/rosetta-translator>


Documentation
-------------

### Installation

```
git clone https://github.com/ondrejsika/rosetta-translator.git
cd rosetta-translator
virtualenv env
./env/bin/pip install -r requirements.txt
./manage.py syncdb
./manage.py collectstatic --noinput
```

### Run

```
./manage.py runserver
```

### Configuration

Locale files add to `locale` directory in project root.

For example:

```
locale/cs/LC_MESSAGES/django.po
locale/de/LC_MESSAGES/django.po
```

Users can access to rosetta mus be in group __translators__.

========
 Harold
========

Harold is what might happen if Kitsune and Fjord were thrown into a
particle accelerator and smashed into each other.


Running it
==========

Local development
-----------------

**Not for production!**

1. Create a virtual environment
2. Run::

       pip install -r requirements-dev.txt

3. Set up the database::

       manage.py migrate

4. Start the server::

       manage.py runserver


Running on Heroku
-----------------

Set ``DJANGO_SETTINGS_MODULE`` env var::

    heroku config:set DJANGO_SETTINGS_MODULE=harold.settings.heroku

Set the ``SECRET_KEY`` env var::

    heroku config:set SECRET_KEY=<some value>

FIXME: More than that?

Then push it to Heroku::

    git push heroku master


Licenses
========

Harold
    Harold is licensed under the MPLv2.

bootstrap
    bootstrap is licensed under the Apache v2 license:
    https://github.com/twbs/bootstrap/blob/master/LICENSE

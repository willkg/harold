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

3. Set up the db. Harold uses `dj-database-url
   <https://github.com/kennethreitz/dj-database-url>`_ and defaults to
   a sqlitedb named``harold.db``.

   Set the database with the ``DATABASE_URL`` environment variable.

4. Set the ``SECRET_KEY`` environment variable.

5. Set up the database::

       manage.py migrate

6. Start the server::

       manage.py runserver


Running on Heroku
-----------------

Set the ``SECRET_KEY``::

    heroku config:set SECRET_KEY=<some value>


FIXME: More than that?

Licenses
========

Harold
    Harold is licensed under the MPLv2.

bootstrap
    bootstrap is licensed under the Apache v2 license:
    https://github.com/twbs/bootstrap/blob/master/LICENSE

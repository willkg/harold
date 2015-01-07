========
 Harold
========

Harold is what might happen if Kitsune and Fjord were thrown into a
particle accelerator and smashed into each other.


Running it
==========

Local development
-----------------

1. Create a virtual environment
2. Run::

       pip install -r requirements-dev.txt

3. Set up the db. Uses `dj-database-url
   <https://github.com/kennethreitz/dj-database-url>`_ and defaults to
   a sqlitedb named``harold.db``. Set the database with the ``DATABASE_URL``
   environment variable and run::

       manage.py syncdb

4. Start the server::

       manage.py runserver


Running on Heroku
-----------------

FIXME - add directions


Licenses
========

Harold
    Harold is licensed under the MPLv2.

bootstrap
    bootstrap is licensed under the Apache v2 license:
    https://github.com/twbs/bootstrap/blob/master/LICENSE

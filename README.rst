.. image:: https://img.shields.io/pypi/v/flask_replicated.svg
        :target: https://pypi.python.org/pypi/flask_replicated

SUMMARY
-------

Flask replicated is a Flask extension, designed to work with
SqlAlchemy. It's purpose it to provide more or less automatic
master-slave replication. On each request, extension determines database
usage intention (to read or to write into a database). Then, it picks
right database url inside overriden ``db.get_engine()`` whenever request
handler tries to access database depending on REST verb used.

Flask replicated comes with a security kill-switch to enable developper mode
to easily keep control on the feature ``AUTO_READ_ON_SLAVE`` true by default,
once deactivated only master database will be used unless explicit use of the decorators.

INSTALLATION
------------

1. Install flask replicated distribution using ``pip install flask_replicated``.
   Or add ``flask-replicated==1.4`` in requirements.txt and requirements
   ``pip3 install -r requirements.txt``.

2. Import library ``from flask_replicated import FlaskReplicated`` or
   ``import flask_replicated`` depending on how you want to call the functions or decorators

3. In flask ``app.config`` configure your database bindings a standard way::

       AUTO_READ_ON_SLAVE = True
       SQLALCHEMY_DATABASE_URI = '%(schema)s://%(user)s:%(password)s@%(master_host)s/%(database)s'
       SQLALCHEMY_BINDS = {
           'master': SQLALCHEMY_DATABASE_URI,
           'slave': '%(schema)s://%(user)s:%(password)s@%(slave_host)s/%(database)s'
       }

4. Register app extension::

       app = Flask(...)
       ...
       FlaskReplicated(app)

USAGE
-----

Flask replicated routes SQL queries into different databases based on
request method. If method is one of ``READONLY_METHODS`` which are defined
as set(['GET', 'HEAD']) and config ``AUTO_READ_ON_SLAVE`` has not been set

While this is usually enough there are cases when DB access is not
controlled explicitly by your business logic. Good examples are implicit
creation of sessions on first access, writing some bookkeeping info,
implicit registration of a user account somewhere inside the system.
These things can happen at arbitrary moments of time, including during
GET requests.

To handle these situations wrap appropriate view function with
``@flask_replicated.use_master_database`` decorator. It will mark function to
always use master database url.

Conversely, wrap the view function with the ``@flask_replicated.use_slave_database``
decorator if you want to ensure that it always uses the slave replica.



GET after POST
~~~~~~~~~~~~~~

There is a special case that needs addressing when working with
asynchronous replication scheme. Replicas can lag behind a master
database on receiving updates. In practice this mean that after
submitting a POST form that redirects to a page with updated data this
page may be requested from a slave replica that wasn't updated yet. And
the user will have an impression that the submit didn't work.

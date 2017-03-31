from setuptools import setup


readme = """
SUMMARY
-------

Flask\_replicated is a Flask extension, designed to work with
SqlAlchemy. It's purpose it to provide more or less automatic
master-slave replication. On each request, extension determines database
usage intention (to read or to write into a database). Then, it picks
right database url inside overriden db.get\_engine() whenever request
handler tries to access database.

INSTALLATION
------------

1. Install flask\_replicated distribution using "python setup.py
   install".

2. In flask app.config configure your database bindings a standard way:

   ::

       SQLALCHEMY_DATABASE_URI = '%(schema)s://%(user)s:%(password)s@%(master_host)s/%(database)s'
       SQLALCHEMY_BINDS = {
           'master': SQLALCHEMY_DATABASE_URI,
           'slave': '%(schema)s://%(user)s:%(password)s@%(slave_host)s/%(database)s'
       }

3. Register app extension:

   ::

       app = Flask(...)
       ...
       FlaskReplicated(app)

USAGE
-----

Flask\_replicated routes SQL queries into different databases based on
request method. If method is one of READONLY\_METHODS which are defined
as set(['GET', 'HEAD'])

While this is usually enough there are cases when DB access is not
controlled explicitly by your business logic. Good examples are implicit
creation of sessions on first access, writing some bookkeeping info,
implicit registration of a user account somewhere inside the system.
These things can happen at arbitrary moments of time, including during
GET requests.

To handle these situations wrap appropriate view function with
@flask\_replicated.changes\_database decorator. It will mark function to
always use master database url.

GET after POST
~~~~~~~~~~~~~~

There is a special case that needs addressing when working with
asynchronous replication scheme. Replicas can lag behind a master
database on receiving updates. In practice this mean that after
submitting a POST form that redirects to a page with updated data this
page may be requested from a slave replica that wasn't updated yet. And
the user will have an impression that the submit didn't work.
"""


setup(
    name='flask_replicated',
    description=(
        'Flask SqlAlchemy router for stateful master-slave replication'
    ),
    long_description=readme,
    author='Peter Demin',
    author_email='peterdemin@gmail.com',
    url='https://github.com/peterdemin/python-flask-replicated',
    license="BSD",
    zip_safe=False,
    keywords='flask sqlalchemy replication master slave',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    version='1.2',
    py_modules=['flask_replicated'],
)

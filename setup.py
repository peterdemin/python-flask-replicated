from distutils.core import setup


with open('README.rst') as fp:
    readme = fp.read()


setup(
    name='flask_replicated',
    description=(
        'Flask SqlAlchemy router for stateful master-slave replication'
    ),
    long_description=readme,
    author='Peter Demin',
    author_email='poslano@gmail.com',
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
    version='1.0',
    py_modules=['flask_replicated'],
)

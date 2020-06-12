from setuptools import setup


with open('README.rst') as fp:
    readme = fp.read()


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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    version='1.4',
    py_modules=['flask_replicated'],
)

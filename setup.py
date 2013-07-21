import sys
if len(sys.argv) == 1:
    sys.argv.append('install')

try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(
    name='pypyodbc-informixcsdk',
    version='1.1.5-rkl20130721-3',
    description='A Pure Python ctypes ODBC module (with Informix Client SDK for Mac OS X support)',
    author='Rockallite Wulf',
    author_email='rockallite.wulf@gmail.com',
    url='https://github.com/rockallite/pypyodbc-informixcsdk',
    py_modules=['pypyodbc'],
      long_description="""\
      A Pure Python ctypes ODBC module compatible with PyPy and almost totally same usage as pyodbc.
      This version supports Informix Client SDK for Mac OS X.
      """,
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
      ],
      keywords='Python, Database, Interface, ODBC, PyPy',
      license='MIT',
      install_requires=[
        'setuptools',
      ],
      )

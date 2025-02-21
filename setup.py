import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pgcli/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

description = 'CLI for Postgres Database. With auto-completion and syntax highlighting.'


setup(
        name='pgcli',
        author='Amjith Ramanujam',
        author_email='amjith[dot]r[at]gmail.com',
        version=version,
        license='LICENSE.txt',
        url='http://pgcli.com',
        packages=find_packages(),
        package_data={'pgcli': ['pgclirc',
                                'packages/pgliterals/pgliterals.json']},
        description=description,
        long_description=open('README.rst').read(),
        install_requires=[
            'pgspecial>=1.1.0',
            'click >= 4.1',
            'Pygments >= 2.0',  # Pygments has to be Capitalcased. WTF?
            'prompt_toolkit==0.46',
            'psycopg2 >= 2.5.4',
            'sqlparse == 0.1.16',
            'configobj >= 5.0.6'
            ],
        entry_points='''
            [console_scripts]
            pgcli=pgcli.main:cli
        ''',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: Unix',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: SQL',
            'Topic :: Database',
            'Topic :: Database :: Front-Ends',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        )

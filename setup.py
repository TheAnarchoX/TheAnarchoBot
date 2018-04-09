from setuptools import setup
from os import system

system('pip install -r requirements.txt')
setup(
    name='TheAnarchoBot',
    version='0.1',
    packages=['bs4', 'bs4.tests', 'bs4.builder',
              'mako', 'mako.ext', 'alembic',
              'alembic.ddl', 'alembic.util',
              'alembic.script', 'alembic.runtime',
              'alembic.testing', 'alembic.testing.plugin',
              'alembic.operations', 'alembic.autogenerate',
              'dateutil', 'dateutil.tz',
              'dateutil.parser', 'dateutil.zoneinfo',
              'markupsafe'],
    url='https://github.com/TheAnarchoX/TheAnarchoBot',
    license='MIT',
    author='Jim "TheAnarchoX" de Vries',
    author_email='jimdvries@gmail.com',
    description='Reddit Bot'
)

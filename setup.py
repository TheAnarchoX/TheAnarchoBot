from setuptools import setup

setup(
    name='TheAnarchoBot',
    version='0.1',
    packages=['venv.Lib.site-packages.mako', 'venv.Lib.site-packages.mako.ext', 'venv.Lib.site-packages.alembic',
              'venv.Lib.site-packages.alembic.ddl', 'venv.Lib.site-packages.alembic.util',
              'venv.Lib.site-packages.alembic.script', 'venv.Lib.site-packages.alembic.runtime',
              'venv.Lib.site-packages.alembic.testing', 'venv.Lib.site-packages.alembic.testing.plugin',
              'venv.Lib.site-packages.alembic.operations', 'venv.Lib.site-packages.alembic.autogenerate',
              'venv.Lib.site-packages.dateutil', 'venv.Lib.site-packages.dateutil.tz',
              'venv.Lib.site-packages.dateutil.parser', 'venv.Lib.site-packages.dateutil.zoneinfo',
              'venv.Lib.site-packages.markupsafe'],
    url='https://github.com/TheAnarchoX/TheAnarchoBot',
    license='MIT',
    author='Jim "TheAnarchoX" de Vries',
    author_email='jimdvries@Gmail.com',
    description='Reddit Bot'
)

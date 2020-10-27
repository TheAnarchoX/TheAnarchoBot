# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='TheAnarchoBot',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='Reddit bot',  # Required

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url='https://github.com/TheAnarchoX/TheAnarchoBot',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author="Jim 'TheAnarchoX' de Vries",  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='jimdvries@gmail.com',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Reddit Developers',
        'Topic :: Software Development :: Python',
        'Topic :: Software Development :: Reddit Bots',
        'Topic :: Software Development :: Python Bots',
        'Topic :: Software Development :: Server Scripting',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='reddit, bot, TheAnarchoX',  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'alembic==0.9.9',
        'asn1crypto==0.24.0',
        'asyncssh==1.11.1',
        'beautifulsoup4==4.6.0',
        'bs4==0.0.1',
        'certifi==2018.1.18',
        'cffi==1.11.4',
        'chardet==3.0.4',
        'cryptography==3.2',
        'idna==2.6',
        'ktcal2==0.1.7',
        'Mako==1.0.7',
        'MarkupSafe==1.0',
        'numpy==1.13.3',
        'praw==5.4.0',
        'prawcore==0.14.0',
        'pycparser==2.18',
        'PyMySQL==0.8.0',
        'python-dateutil==2.7.2',
        'python-editor==1.0.3',
        'requests==2.20.0',
        'six==1.11.0',
        'SQLAlchemy==1.2.6',
        'update-checker==0.16',
        'urllib3==1.24.2',
    ],  # Optional

    project_urls={  # Optional
        'Source': 'https://github.com/TheAnarchoX/TheAnarchoBot/',
    },
)

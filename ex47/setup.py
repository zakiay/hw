try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Zaki Ahmed Yahia',
    'url': 'github.com/zakiay/hw',
    'download_url': 'github.com/zakiay/hw',
    'author_email': 'zakiay.su@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
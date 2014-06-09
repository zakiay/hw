try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Zaki Ahmed Yahia',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'zakiay.su@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
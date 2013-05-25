from distutils.core import setup
from log_io_handler import VERSION,AUTHOR,EMAIL,URL

setup (
    name = "log_io_handler",
    author = AUTHOR,
    author_email = EMAIL,
    url = URL,
    version = VERSION,
    packages = ['log_io_handler',],
    license = 'GPL v3 or higher',
    long_description = open('README.txt').read(),
)

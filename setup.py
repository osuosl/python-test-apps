from distutils.core import setup
from setuptools import find_packages

dependencies = [
    'Django==1.7.4',
]

setup(
    name='python-test-apps',
    version='1.0.0',
    install_requires=dependencies,
    author='OSU Open Source Lab'
    author_email='support@osuosl.org',
    packages=find_packages(),
    url='https://github.com/osuosl/python-test-apps',
    license='Apache 2',
    description='',
    long_description=open('README.rst').read()
)

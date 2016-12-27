# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='takeoff', # FIXME
    version='0.1.0',
    description='An easy to use project template for Python', # FIXME
    long_description=readme,
    author='Ivan Dmitrievsky', # FIXME
    author_email='ivan.dmitrievsky+python@gmail.com', # FIXME
    url='https://github.com/idmit/takeoff', # FIXME
    install_requires=[
        # FIXME
    ],
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

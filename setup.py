import os
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='hdv_mailer',
        packages=["hdv_mailer"],
        version='0.0.1',
        author='Alex Hyojun Kim',
        author_email='alex@hotdev.com',
        description='Simple wrapper class for emails',
        license=license,
        long_description=readme,
        install_requires=[
            'emails==0.5.13',
            'hdv_dummy'
            ],
        entry_points={}
      )
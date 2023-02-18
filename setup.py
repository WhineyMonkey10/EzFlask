from setuptools import setup

setup(
   name='ezFlask',
   version='0.1.0',
   author='WhMonkey',
   packages=['ezFlask'],
   license='LICENSE.txt',
   description='An easy to use flask wrapper.',
   long_description=open('README.md').read(),
   install_requires=[
       "flask",
       "flask_cors",
   ],
)
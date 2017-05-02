'Computer vision as a Service - Python Client'

from setuptools import setup

setup(
    name='cvas',
    version='1.1.28',
    description='Computer Vision as a Service Python Client',
    long_description='Computer Vision as a Service Python Client.',
    license='MIT',
    author='Adam Jez',
    author_email='adamjez@outlook.cz',
    packages=['cvas'],
    install_requires=[
        'requests',
        'json',
        'tempfile'
    ]
)

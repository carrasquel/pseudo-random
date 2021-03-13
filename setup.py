# setup.py

from setuptools import setup

setup(name='CoolRandom',
    version='0.1',
    description='A Python package for pseudo random numbers generation',
    url='https://github.com/carrasquel/pseudo-random',
    author='Nelson Carrasquel',
    author_email='carrasquel@outlook.com',
    license='MIT',
    packages=['pseudorandom'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False)
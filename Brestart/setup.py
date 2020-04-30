# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:14:06 2020

@author: Administrator
"""
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(name='Brestart',
      version='0.1',
      description='restart functions at breakpoint',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/lvws/python-breakpoint-restart-Python-',
      author='Wansheng.Lv',
      author_email='1129309258@qq.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.6',
      zip_safe=False)

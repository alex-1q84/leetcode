# -*- coding:utf-8 -*-
import sys
sys.path.append('./src')
from distutils.core import setup
from leetcode import __version__

setup(name='leetcode',
      version=__version__,
      description='empty python project template',
      long_description=open("README.md").read(),
      author='hailxl',
      author_email='hailxl@gmail.com',
      packages=['leetcode'],
      package_dir={'leetcode': 'src/leetcode'},
      #package_data={'leetcode': ['stuff']},
      license="Public domain",
      platforms=["any"],
      url='https://github.com/hailxl/leetcode')

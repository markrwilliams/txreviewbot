"""
Setup file for txreviewbot.
"""

from setuptools import setup, find_packages

setup(name='txreviewbot',
      use_incremental=True,
      setup_requires=['incremental'],
      install_requires=['incremental',
                        'six',
                        'Twisted>=16.6.0'],
      packages=find_packages() + ['twisted.plugins'],
      include_package_data=True,
      license="MIT")

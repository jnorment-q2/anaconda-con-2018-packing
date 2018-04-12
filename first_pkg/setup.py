
#!/usr/bin/env python

from setuptools import setup

setup(name='mypkg',
      version='1.0',
      # list folders, not files
      packages=['mypkg', 'mypkg.subpkg'],
     )

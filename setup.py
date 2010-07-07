# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '1.0'

setup(name='ploneexample.cprestrictions',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n",
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Israel Saeta Pérez',
      author_email='israel.saeta@dukebody.com',
      url='http://svn.plone.org/svn/collective/ploneexample.cprestrictions',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneexample'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      )

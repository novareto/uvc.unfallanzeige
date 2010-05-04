from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='uvc.widgets',
      version=version,
      description="A collection of widgets for formlib / z3cformm based on jquery",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'hurry.jqueryui',
          'megrok.resource',
          'hurry.jquery',
          'hurry.zopetinymce',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

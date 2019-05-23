# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name='inputao',
      version='1.2',
      description='Um input melhor para ajudar os iniciantes em Python.',
      long_description=open(README).read(),
      long_description_content_type="text/markdown",
      author="Henrique Bastos", author_email="henrique@bastos.net",
      license="MIT",
      keywords=['input', 'beginner', 'tool'],
      packages=['inputao'],
      package_dir={"inputao": "inputao"},
      zip_safe=True,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Portuguese',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
          'Topic :: Software Development :: Libraries',
      ],
      url='http://github.com/henriquebastos/inputao/',)

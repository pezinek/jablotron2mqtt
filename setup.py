from setuptools import setup

setup(name='jablotron',
      version='0.1',
      description='Library for interfacing with jablotron 6x alarms',
      url='https://github.com/pezinek/py-jablotron6x',
      packages=['jablotron'],
      install_requires=[
        'pySerial',
      ],
      zip_safe=False,
)


from setuptools import setup

setup(
  name='xls2txt',
  version='0.0.1',
  py_modules=['xls2txt'],
  entry_points={
    'console_scripts':[
      'xls2txt = xls2txt:main',
    ]
  }
)


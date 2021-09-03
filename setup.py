from distutils.core import setup
from setuptools import find_packages
from pynaja import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(name=r'pynaja',
      version=__version__,
      license=r'Apache License Version 2.0',
      author=r'xiami',
      author_email=r'gaohlsilence@163.com',
      description=r'Async Suite For Python',
      long_description=long_description,
      long_description_content_type=r'text/markdown',
      url=r'https://github.com/xiaoxiamiya/naja.git',
      packages=find_packages(),
      package_data={r'najapy': [r'static/*.*', r'scaffold/fastapi_example_project/fastapi_example/conf/*.*']},
      python_requires=r'>= 3.8',
      platforms=[r"all"],
      install_requires=[
          r'APScheduler==3.7.0',
          r'PyJWT==2.0.1',
          r'SQLAlchemy==1.3.23',
          r'WTForms==2.3.3',
          r'aiohttp==3.7.4',
          r'aiomysql==0.0.21',
          r'aioredis==1.3.1',
          r'async-timeout==3.0.1',
          r'cachetools==4.2.1',
          r'cryptography==3.4.6',
          r'fastapi==0.66.1',
          r'gunicorn==20.1.0',
          r'hiredis==1.1.0',
          r'httptools==0.1.1',
          r'loguru==0.5.3',
          r'motor==2.3.1',
          r'ujson==4.0.2',
          r'pytz==2021.1',
          r'PyMySQL==0.9.3',
          r'pymongo==3.12.0',
          r'uvicorn==0.14.0',
          r'xmltodict==0.12.0',
          r'psutil==5.8.0',
      ],
      classifiers=[
          r'Programming Language :: Python :: 3.8',
          r'License :: OSI Approved :: Apache Software License',
          r'Operating System :: POSIX :: Linux',
      ],
      )

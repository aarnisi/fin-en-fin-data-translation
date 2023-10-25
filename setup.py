from setuptools import setup, find_packages

setup(
    name='translate',
    version='1.0.0',
    url = 'https://github.com/aarnisi/fin-en-fin-data-translation/',
    packages=find_packages(),
    install_requires=[
        'pandas'
       ,'transformers'
       ,'TensorFlow'
    ],
)

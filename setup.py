'''Module setup'''
from setuptools import setup

'''
packaging modeled after
https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
'''


def read(filename):
    '''Read content from file'''
    return open(filename).read()

setup(
    name='vultr_api',
    version='1.0.1',
    install_requires=[
        "requests"
    ],
    description='Vultr.com API Client',
    long_description=(read('README.md')),
    long_description_content_type='text/markdown',
    url='http://github.com/rsp2k/python-vultr',
    author='Darrel O\'Pry',
    author_email='darrel.opry@spry-group.com',
    packages=['vultr_api'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license=read('LICENSE'),
    test_suite='tests'
)

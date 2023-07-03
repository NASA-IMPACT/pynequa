from setuptools import setup, find_packages

VERSION = '0.1.0'
requirements = []
test_requirements = ['pytest>=3']

setup(
    name='sinequa_py',
    version=VERSION,
    author='Anish Bhusal',
    author_email='anish.bhusal@uah.edu',
    description='Pythonic Layer for Sinequa REST API',
    packages=find_packages(include=['sinequa_py', 'sinequa_py.*']),
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
)

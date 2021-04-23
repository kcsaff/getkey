# -*- coding: utf-8 -*-

import sys
import io
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from getkey import __version__


def read_description():
    with io.open('README.rst', encoding='utf-8') as fd:
        return fd.read()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['--cov-report=term-missing']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='getkey',
    version=__version__,
    description="Read single characters and key-strokes",
    long_description=read_description(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    keywords='stdin,command line',
    author='K.C.Saff',
    author_email='kc@saff.net',
    url='https://github.com/kcsaff/getkey',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tools', 'venv']),
    include_package_data=True,
    zip_safe=False,
    cmdclass={'test': PyTest},
    tests_require=[
        'doublex  >= 1.8.1',
        'pexpect  >= 3.3',
        'coverage >=3.7.1,<4.0a1',

        'pytest     >= 2.6.2',
        'pytest-cov >= 1.8.0',

        'python-coveralls >= 2.5.0',
        'wheel >= 0.24.0',
    ],
    install_requires=[
    ],
    setup_requires=[
        'flake8',
    ],
)

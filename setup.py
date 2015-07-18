# Attr utils, (C) 2015 Harshavardhana.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

version = '0.1.0'

setup(
    name='attr-utils',
    version=version,
    description='attr-utils in Python, getfattr/setfattr cross platform implementations',
    author='Harshavardhana',
    author_email='harsha@harshavardhana.net',
    install_requires=['xattr'],
    url='https://github.com/harshavardhana/attr-utils.git',
    license='Apache License 2.0',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    scripts=['getfattr.py', 'setfattr.py'],
    long_description=long_description,
)

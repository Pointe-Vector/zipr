from setuptools import setup, find_namespace_packages

setup(
    name='zipr-http',
    version='0.0.2',
    author='Andrew Hoekstra',
    author_email='andrew@pointevector.com',
    url='https://github.com/Pointe-Vector/zipr',
    packages=find_namespace_packages(include=['zipr.*']),
    install_requires=[
        'zipr-core',
    ],
    entry_points={'zipr.plugins': 'Http = zipr.http'},
)

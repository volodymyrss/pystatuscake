from setuptools import setup, find_packages

setup(
    name='pystatuscake',
    version='0.1.0',
    url='https://github.com/volodymyrss/pystatuscake.git',
    author='Volodymyr Savchenko',
    author_email='vladimir.savchenko@gmail.com',
    description='an alternative statuscake, more command line, more simple',
    packages=find_packages(),    
    install_requires=['requests'],
    entry_points={
            'console_scripts': [
                'scake = statuscake.cli:main'
            ]
    }
)

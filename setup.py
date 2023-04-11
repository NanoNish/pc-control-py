from setuptools import setup

setup(
    name='index',
    version='0.1.0',
    py_modules=['index'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'index = index:start',
        ],
    },
)
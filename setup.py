from setuptools import setup

setup(
    name='tlsscan',
    version='0.1',
    py_modules=['tlsscan'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tlsscan=tlsscan:scan
    ''',
)

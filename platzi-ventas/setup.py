from setuptools import setup

setup(
    name='pv', #el nombre con el que se va a invocar
    version='0.1', # version
    py_modules=['pv'], #este es el modulo pv
    install_requires=[
        'Click',
    ], #como requisito libreria click
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)
#cli punto de entrada
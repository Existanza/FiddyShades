__author__ = 'Deca'
from cx_Freeze import setup, Executable

setup(
    name='FiddyShades',
    version="1",
    description="Picture/text converter",
    executables=[Executable("__init__.py")],
    )
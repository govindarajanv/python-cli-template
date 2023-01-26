from setuptools import setup

setup(
    name='dcp',
    version=1.0,
    packages=['dcp'],
    install_requires=['click', 'pytest'],
    entry_points={'console_scripts': ['dcp = dcp.cli:cli']}
)
from setuptools import setup, find_packages

setup(
    name = "rca",
    version = "0.1",
    packages = find_packages(exclude=['tests']),
    scripts = ['rca.py']
    )
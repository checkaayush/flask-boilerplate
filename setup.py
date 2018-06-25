# Reference: https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages


def requirements():
    """Returns packages required by current project."""
    reqs = []
    with open('requirements.txt', 'r') as f:
        for line in f:
            if line.startswith('git+https'):
                continue
            reqs.append(line.strip())
    return reqs


def packages():
    """Returns list of packages inside current project."""
    return find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])


setup(
    name='skaffold',
    version='0.1',
    description='',
    url='https://github.com/checkaayush/flask-boilerplate',
    author='Aayush Sarva',
    author_email='checkaayush@gmail.com',
    packages=packages(),
    install_requires=requirements()
)

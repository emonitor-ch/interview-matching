from setuptools import find_packages, setup

import src

setup(
    name='emonitor-matrix',
    version=src.__version__,
    description="A square matrix matching solver (similar to bipartite graph)",
    author=src.__author__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'src = src.__main__:main',
        ],
    },
    python_requires='>=3.9'
)
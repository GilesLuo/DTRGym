import os
from setuptools import find_packages, setup


def get_version() -> str:
    init = open(os.path.join("DTRGym", "__init__.py"), "r").read().split()
    return init[init.index("__version__") + 2][1:-1]


def get_install_requires():
    return [
        "torch>=1.13",
        "numpy==1.25.*",
        "tianshou==0.5.0",
        "simglucose==0.2.3",
        "urllib3",
        "packaging",
        "tqdm",
        "matplotlib",
        "scipy",
        "pandas",
        "gymnasium",
        "gym",
    ]


def get_extras_require():
    req = {
        "dev": [
            "flake8",
            "pytest",
            "pytest-cov",
            "mypy",
        ],
    }
    return req


setup(
    name='DTRGym',
    version=get_version(),
    python_requires="== 3.10.*",
    description='A Collection of Reinforcement Learning Environments for Dynamic Treatment Regime Simulation.',
    author='Zhiyao Luo, Mingcheng Zhu',
    author_email='zhiyao.luo@eng.ox.ac.uk',
    url='http://github.com/GilesLuo/DTRGym',
    packages=find_packages(
        exclude=["test", "test.*", "examples", "examples.*", "docs", "docs.*"]
    ),
    install_requires=get_install_requires(),
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords=["Healthcare Simulation", "Dynamic Treatment Regime", "Reinforcement Learning"],
    extras_require=get_extras_require(),
    project_urls={
        "Source Code": "https://github.com/GilesLuo/DTRGym",
    }
)

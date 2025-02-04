from setuptools import find_packages, setup

setup(
    name="democicd",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "democicd = democicd.main:main",
        ],
    },
)

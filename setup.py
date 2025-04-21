from setuptools import setup, find_packages

setup(
    name="Ancient-Language-Processing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # list the dependencies here
        "numpy==1.23.5",
        # other dependencies from requirements.txt
    ],
    entry_points={
        'console_scripts': [
            # add any CLI commands here
        ]
    },
)
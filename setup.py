from setuptools import setup, find_packages

setup(
    name="netpicker_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Sanjay Kumar",
    description="SDK for interacting with the Netpicker API",
    python_requires='>=3.7',
)

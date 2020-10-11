import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="TDW8970",
    version="0.1.0",
    description="A library for scraping ADSL connection statistics from TD-W8970 router. ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/morsisko/TD-W8970",
    author="morsisko",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
    ],
    packages=["TDW8970"],
)

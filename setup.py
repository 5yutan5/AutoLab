from setuptools import find_packages, setup

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="AutoLab",
    version="0.1.0",
    author="Yakitori",
    author_email="4yutan4@gmail.com",
    description="This module help creating GUI application useing for experiments.",
    longdescription=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/5yutan5/AutoLab",
    include_package_data=True,
    packages=find_packages(exclude="tests"),
    package_data={"style": ["AutoLab/style/*.qss"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

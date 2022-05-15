#!/usr/bin/env python3

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ichika-utils",
    version="0.1.0",
    author="No767",
    description="Stats Utils for Ichika - Package to process and calculate statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/No767/Ichika-Utils",
    project_urls={
        "Bug Tracker": "https://github.com/No767/Ichika-Utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Science/Research"
        
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7,<3.11",
    
    
)
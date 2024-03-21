import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smi-utilities",
    version="1.0.0",
    author="Ricardo Palma",
    author_email="rpalma@enerlink.com",
    description="Get utilities for SMI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rpalmaener/smi.git",
    project_urls={
        "Bug Tracker": "https://github.com/rpalmaener/smi.git"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7"
)

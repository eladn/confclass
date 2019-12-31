import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='confclass',
    version='0.1',
    scripts=['confclass.py'],
    author="Elad Nachmias",
    author_email="eladnah@gmail.com",
    description="A python package for working with program configuration parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eladn/confclass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )

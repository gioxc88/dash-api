
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dash-api", # Replace with your own username
    version="0.0.1",
    author="gioxc88",
    author_email="gioxc@hotmail.it",
    description="A new api for dash layout",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gioxc88/dash-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'dash>=1.0.1'

    ]
)
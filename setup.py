
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dash-wrapper", # Replace with your own username
    version="0.0.3",
    author="gioxc88",
    author_email="gioxc@hotmail.it",
    description="A wrapper around dash to extend the api defining the layout",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gioxc88/dash-wrapper",
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
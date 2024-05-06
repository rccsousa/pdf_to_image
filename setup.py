from setuptools import find_packages, setup

setup(
    name = 'pdf2img',
    version = '0.0.10',
    description = 'A simple script to convert PDF files to images',
    package_dir = {"": "app"},
    packages = find_packages(where = "app"),
    url = 'https://github.com/rezekiz/pdf2img',
    author = 'Rezeki',
    install_requires=[
        "pillow>=10.3.0",
        "PyMuPDF>=1.24.2",
        "PyMuPDFb>=1.24.1"
    ],
    python_requires = ">=3.10" )
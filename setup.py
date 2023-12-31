# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import requests

# To use a consistent encoding
from codecs import open
from os import path

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Get library version from pypi.org
def get_current_version():
    url = "https://pypi.org/pypi/honeydew/json"
    response = requests.get(url)
    data = response.json()
    version = data["info"]["version"]
    return version

def increase_version(version=get_current_version()):
    segments = version.split('.')
    last_segment = int(segments[-1])
    last_segment = last_segment + 1
    segments[-1] = str(last_segment)
    new_version = '.'.join(segments)
    return new_version    
    

# This call to setup() does all the work
setup(
    name="honeydew",
    version=increase_version(),
    description="Collection of connectors for ETL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://honeydew-lib.github.io/",
    project_urls = {
        'Repository': 'https://github.com/jeffis-ca/honeydew',
        'Documentation': 'https://honeydew-lib.github.io/'
    },
    author="Poltak Jefferson",
    author_email="poltak.jefferson@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["honeydew"],
    include_package_data=True,
    install_requires=[
        "pandas","numpy","mysql-connector-python","google-cloud","google-auth","google-cloud-bigquery","google-cloud-bigquery-storage","google-cloud-storage",
        "google-cloud-logging","google-cloud-secret-manager","google-cloud-translate", "pandas_gbq", "paramiko", "scp", "pytz", "pigz-python", "clickhouse-connect",
        "mkdocs","mkdocs-material","mkdocs-material-extensions","mkdocstrings","mkdocstrings-python","mkdocs-pymdownx-material-extras","pymdown-extensions","build",
        "twine", "requests", "wheel","gitpython"
                      ]
)
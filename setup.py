from setuptools import setup, find_packages
import os
import subprocess

project_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in project_version

assert os.path.isfile("DjangoRangeMiddleware/version.py")
with open("DjangoRangeMiddleware/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{project_version}\n")


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


# Setting up
setup(
    name="DjangoRangeMiddleware",
    version=project_version,
    author="Aiden (Dev)",
    author_email="",
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description='Django Range Middleware',
    packages=find_packages(),
    url='https://github.com/QuackCoding/DjangoRangeMiddleware',
    package_data={'DjangoRangeMiddleware': ['VERSION']},
    install_requires=[],
    keywords=['python', 'middleware', 'django', 'DjangoRangeMiddleware', 'Range'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
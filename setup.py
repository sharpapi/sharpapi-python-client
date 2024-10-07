from setuptools import setup, find_packages

setup(
    name='sharpapi-python-client',
    version='1.2.0',
    description='SharpAPI.com Python SDK Client - AI-Powered Workflow Automation API.',
    author='Dawid Makowski',
    author_email='contact@sharpapi.com',
    url='https://github.com/sharpapi/sharpapi-python-client',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)


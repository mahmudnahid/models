"""Setup script for object_detection."""

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['Pillow>=1.0',
                     'Matplotlib>=2.1',
                     'Cython>=0.28.1',
                     'Protobuf',
                     'lxml',
                     'jupyter',
                     'matplotlib',
                     'tensorflow',
                     'contextlib2',
                     'tf_slim']

setup(
    name='object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[p for p in find_packages() if p.startswith('object_detection')],
    description='Tensorflow Object Detection Library',
)

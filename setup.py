from setuptools import setup

with open("ReadME.md", "r") as fh:
    long_description = fh.read()

setup(
    name='myplugin',
    version='0.0.1',
    description='say hello!',
    py_modules=["myplugin"],
    packages_dir={'': 'src'},
    entry_points={
        'pytest11': [
            'myplugin = src.myplugin',
        ],
    },
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
        ]
    },
)

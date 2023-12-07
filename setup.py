"""Setup file for the project."""

from setuptools import setup


def readme():
    """Read the README.md file."""
    with open("README.md", encoding="UTF-8") as f:
        return f.read()


setup(
    name="moms-canning-timer",
    version="0.3.0",
    description="Customizable 15-minute stove top timers, \
        created for preserving fruits and veggies for the winter.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    keywords="canning timer clock time gui",
    url="https://github.com/Dog-Face-Development/Moms-Canning-Timer",
    author="willtheorangeguy",
    py_modules=["main"],
    entry_points={"console_scripts": ["canning-timer=main:timer"]},
)

from setuptools import setup

# TODO: Clean up build and egg-info folders after setup, don't know how

setup(
    name="mvp",
    version="1.0.0",
    description="A fancier mv",
    url="https://github.com/1nter-p/mvp",
    author="1nterp",
    license="MIT",
    packages=["mvp"],
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["mvp = mvp.__main__:main"],
    },
)

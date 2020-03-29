import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="optcutfreq",
    version="0.0.8",
    author="Marcos Duarte",
    author_email="duartexyz@gmail.com",
    description="Automatic search of optimal filter cutoff frequency based on residual analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/demotu/optcutfreq",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

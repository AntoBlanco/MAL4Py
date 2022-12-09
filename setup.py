from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="MAL4API",
    version="0.1.1",
    description="MAL4Py is a small package for download and sync information from MyAnimeList.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tony White",
    author_email="tony.white_dev@proton.me",
    url="https://github.com/AntoBlanco/MAL4Py",
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["api","myanimelist","MAL4API","Anime","Manga"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
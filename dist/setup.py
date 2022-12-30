import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reddit_comment_scrapper",
    version="0.0.1",
    author="Prarabdha Srivastava",
    author_email="sriprarabdha2004@gmail.com",
    description="A package for scrapping reddit comments'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SriPrarabdha/reddit-scrapper-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
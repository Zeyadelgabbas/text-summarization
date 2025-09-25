import setuptools







__version__ = "0.0.0"
REPO_NAME = "text-summarization"
AUTHOR_USERNAME = "Zeyadelgabbas"

setuptools(
    name = "textsummarizer",
    version = __version__ ,
    author = AUTHOR_USERNAME,
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}"
    package_dir = {"":"src"}
    packages = setuptools.find_packages(where = 'src')
)
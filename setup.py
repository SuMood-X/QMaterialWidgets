import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PySide6-Material-Widgets",
    version="0.1.0",
    keywords="pyside6 fluent widgets",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A material design widgets library based on PySide6",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/zhiyiYo/PySide-Material-Widgets/tree/master",
    packages=setuptools.find_packages(),
    install_requires=[
        "PySide6<=6.4.2",
        "PySideSix-Frameless-Window",
        "darkdetect",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Documentation': 'https://pyside-material-widgets.readthedocs.io/',
        'Source Code': 'https://github.com/zhiyiYo/PySide-Material-Widgets/tree/master',
        'Bug Tracker': 'https://github.com/zhiyiYo/PySide-Material-Widgets/issues',
    }
)
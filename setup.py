from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from dinject.version import get_version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Utilities",
    "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="",
    entry_points={
        "console_scripts": [
            "dinject=dinject.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    install_requires=[
        "mdcode==1.0.0a1",
        "naughtty~=1.0",
        "thtml~=1.0.5",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="dinject",
    packages=[
        "dinject",
        "dinject.enums",
        "dinject.exceptions",
        "dinject.executors",
        "dinject.types",
        "dinject.version",
    ],
    package_data={
        "dinject": ["py.typed"],
        "dinject.enums": ["py.typed"],
        "dinject.exceptions": ["py.typed"],
        "dinject.executors": ["py.typed"],
        "dinject.types": ["py.typed"],
        "dinject.version": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/dinject",
    version=version,
)

from setuptools import setup, find_packages

setup(
    name="python-venv-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyperclip",
    ],
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "vem=main:main"
        ]
    },
)
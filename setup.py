from setuptools import setup

setup(
    name="python-venv-manager",
    version="0.1",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "vem=main:main"
        ]
    },
)
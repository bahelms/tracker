from setuptools import setup

setup(
    name="Tracker",
    version="0.0.1",
    py_modules=["tracker"],
    install_requires=[
        "click",
    ],
    entry_points="""
        [console_scripts]
        tracker=cli:cli
    """
)

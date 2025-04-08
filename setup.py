from setuptools import setup, find_packages

setup(
    name="oni_sama",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "discord.py>=2.3.2",
        "python-dotenv>=1.0.0",
        "aiohttp>=3.9.1"
    ]
)

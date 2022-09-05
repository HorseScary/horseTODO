from setuptools import setup

setup(name="horsetodo",
    version="0.1.1",
    description="A basic cli todolist script",
    url="https://github.com/HorseScary/horseTODO/",
    author="HorseScary",
    author_email="horsescary@gmail.com",
    license="GPL3",
    packages=["horsetodo"],
    scripts=['bin/horsetodo'],
    zip_safe=True)
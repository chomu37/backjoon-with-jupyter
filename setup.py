from setuptools import setup, find_packages

setup(
    name="bwj",
    version="0.0.4",
    description="Python 과 Jupyter Notebook 을 이용해 [백준 온라인 저지](https://www.acmicpc.net/)를 풀 때 도움을 줄 수 있는 모듈입니다.",
    author="chomu",
    author_email="2chanhaeng@gmail.com",
    packages=["bwj"],
    package_data = {
        'bwj': ['static/*.ipynb'],
    },
    install_requires=["requests", "bs4"],
)
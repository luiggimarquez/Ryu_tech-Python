from setuptools import setup, find_packages

setup(
    name="paquete_preentrega",
    version="1.00",
    description ="Paquete que contiene la primera preentrega y la segunda, la segunda consiste en una clase Cliente con metodos y atributos",
    author="Luiggi Marquez",
    author_email="nf_snake@hotmail.com",
    package_data={'': ['*.ipynb','*.json']},
    packages=find_packages(),

)

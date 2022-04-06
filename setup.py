from setuptools import setup

readme = open("./README.md", "r")

setup(
    name='reqplus',
    packages=['reqplus'],
    version='0.0.2',
    license='GNU v3.0',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    description='A lib for strict Flask reqparse',
    author='dviana',
    author_email='dviana7898@gmail.com',
    url='https://github.com/dviana159/reqplus',
    download_url='https://github.com/dviana159/reqplus/tarball/1.0',
    keywords=['Better flask reqparse', 'reqplus flask'], # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python :: 3.7'],
)
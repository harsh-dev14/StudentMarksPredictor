from typing import List
from setuptools import find_packages,setup

HYPHEN_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return requirements

setup(
    name='mlproj',
    version='0.0.1',
    author='Harsh',
    author_email='devharsh1403@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
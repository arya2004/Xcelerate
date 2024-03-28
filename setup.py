from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_all_requirements(file_path : str) -> List[str]:
    '''
    returns the list of all requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='xcelerate',
    version='0.0.1',
    author='arya2004',
    author_email='arya.pathak@outlook.in',
    packages=find_packages(),
    install_requires=get_all_requirements('requirements.txt')

)
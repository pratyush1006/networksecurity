'''The setup.py file is essential part of packaging and 
distributing Python projects.It is used by setuptools 
to define the package metadaet_requirements(file_path: str) -> List[str]:
    """ta and dependencies.'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            #Process each line 
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
    name='Network_Security',
    version='0.0.1',
    author='Pratyush Deep',
    author_email="pratyushdeep007@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

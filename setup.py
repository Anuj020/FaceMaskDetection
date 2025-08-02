from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    """
        This function will return list of requirements
    """

    requirements_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read line from thr file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
            
            if requirement and requirement!= '-e .':
                requirements_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt not found")
    return requirements_lst

setup(name="Face Mask Detection",
      version="0.0.1",
      author="Anuj Patel",
      author_email="2000anujpatel@gmail.com",
      packages=find_packages(),
      install_requires = get_requirements()
      )

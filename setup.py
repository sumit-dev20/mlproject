from setuptools import find_package, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return list of package which are needed to run this project
    """
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="MLProject",
    version="0.0.1",
    author="Sumit",
    requires=find_package(),
    packages=get_requirements(file_path="requirements.txt"),
)

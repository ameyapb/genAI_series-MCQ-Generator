from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Ameya Patil',
    author_email='ameyapatil2424@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","Wikipedia-API"],
    packages=find_packages()
)
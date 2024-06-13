from setuptools import setup, find_packages

setup(
    name='my_scaffolder',
    version='0.1',
    author='Aryan Rajpurkar and Yash Thakar',
    author_email='av.rajpurkar@gmail.com',
    description='A CLI tool to scaffold different types of Python projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yashyaks/create-py-app',  # Update with your repository URL
    py_modules=['scaffolder'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        create_py_app=scaffolder:cli
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

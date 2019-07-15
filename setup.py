from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='problem-solving-with-algorithm',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="book on problem-solving-with-algorithm",
    author="ansir",
    author_email='an5ir@hotmail.com',
    url='https://github.com/an5ir/problem-solving-with-algorithm',
    packages=['problem-solving-with-algorithm'],
    entry_points={
        'console_scripts': [
            'problem-solving-with-algorithm=problem-solving-with-algorithm.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='problem-solving-with-algorithm',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)

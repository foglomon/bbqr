from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name='bbqr',
    version='0.1.0',
    description='BBQR, the hottest terminal-based QR code generator that grills your data to perfection!',
    author='Ishman Singh',
    py_modules=['bbqr'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bbqr=bbqr:main',
        ],
    },
    install_requires=requirements,
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/foglomon/bbqr',
    },
)
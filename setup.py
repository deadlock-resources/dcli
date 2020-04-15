import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deadlock-cli",
    version="1.1.3",
    author="Slayug",
    author_email="apuret@takima.fr",
    description="CLI tools for Deadlock challenges.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deadlock-resources/dcli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    packages=setuptools.find_packages(),
    scripts=['scripts/dcli'],
    install_requires=[
        'inquirer',
        'PyInquirer',
        'fire',
        'Jinja2',
        'colored',
        'Flask',
        'request',
        'jsonify',
        'requests',
        'pyyaml'
    ],
    python_requires='>=3.2',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dcli",
    version="0.0.8",
    author="Deadlock",
    author_email="apuret@takima.fr",
    description="CLI tools for Deadlock challenges.",
    long_description="Tools to create, run your Deadlock challenges",
    long_description_content_type="text/markdown",
    url="https://github.com/Deadlock/cli-tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
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
        'colored'
    ],
    python_requires='>=3.2',
)

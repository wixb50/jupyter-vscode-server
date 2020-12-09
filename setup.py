import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter-vscode-server",
    version="0.1.0",
    author="wixb50",
    author_email="wixb50@gmail.com",
    description="A Jupyter extension to launch VS Code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wixb50/jupyter-vscode-server",
    py_modules=['nbvscode'],
    entry_points={
        'jupyter_serverproxy_servers': [
            'nbvscode = nbvscode:setup_nbvscode',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux ",
    ],
    install_requires=['jupyter-server-proxy'],
)

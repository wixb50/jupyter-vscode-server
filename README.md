# Jupyter VS Code Server

## About jupyter-vscode-server

A Jupyter Notebook extension to launch [cdr/code-server](https://github.com/cdr/code-server) (VS Code).

## Using jupyter-vscode-server

You must already have code-server installed. Check out code-server's [Getting Started](https://github.com/cdr/code-server#getting-started) section.

Extension can be install with:

```bash
pip install git+https://github.com/wixb50/nbvscode.git
```

Example Dockerfile segment to install code-server:

```Dockerfile

ENV CODE_WORKINGDIR=/home/jovyan \
    CODE_EXTENSIONSDIR=/home/jovyan/.vscode_extensions \
    CODE_USERDATADIR=/home/jovyan/.vscode_data

RUN mkdir -p /opt/code-server && \
    wget -qO- http://172.21.54.223:8071/code-server-3.7.4-linux-amd64.tar.gz | tar zxvf - --strip-components=1 -C /opt/code-server && \
    ln -s /opt/code-server/bin/code-server /usr/local/bin/code-server
```

Then you can access by `/nbvscode` or New `VS Code` at tree page.

## Install Extension Example

```
code-server --install-extension ms-python.python --extensions-dir $CODE_EXTENSIONSDIR
```

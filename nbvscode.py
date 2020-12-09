import os


def setup_nbvscode():
    working_dir = os.getenv("CODE_WORKINGDIR", ".")

    extensions_dir = os.getenv("CODE_EXTENSIONSDIR", None)
    user_data_dir = os.getenv("CODE_USERDATADIR", None)

    cmd = ["code-server", "--port", "{port}",
           "--auth", "none", "--disable-telemetry"]

    if extensions_dir:
        cmd += ["--extensions-dir", extensions_dir]

    if user_data_dir:
        cmd += ["--user-data-dir", user_data_dir]

    cmd.append(working_dir)
    return {
        "command": cmd,
        "timeout": 20,
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }

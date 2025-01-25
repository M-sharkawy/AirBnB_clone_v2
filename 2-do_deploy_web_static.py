#!/usr/bin/python3
'''module to deploy the program version'''

from fabric.api import *

env.user = "ubuntu"
env.hosts = ['100.26.253.64', '54.152.64.223']


def do_deploy(archive_path):
    '''deploy the archived files'''

    if not archive_path:
        return False

    file_name = archive_path.split("/")[-1]
    no_ext = file_name.replace(".tgz", "")
    remote_path = "/tmp/"
    _path = f"/data/web_static/releases/{no_ext}"

    try:
        put(archive_path, remote_path)
        run(f"mkdir -p {_path}")
        run(f"tar -xzvf {file_name} -C {_path}")
        run(f"rm -f {remote_path}{file_name}")
        run(f"mv {_path}/web_static/* {_path}")
        run(f"rm -rf {_path}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {_path} /data/web_static/current")
        return True

    except Exception:
        return False

#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of
the web_static folder of the AirBnB Clone repo'''

from fabric.api import *
from datetime import datetime
import os.path

env.user = 'ubuntu'
env.hosts = ['100.26.253.64', '54.152.64.223']


def do_pack():
    '''do packer'''
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local(f"tar -c --verbose -z --file={file_name} ./web_static")
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    '''deploy the archived files'''

    if os.path.exists(archive_path) is False:
        return False

    file_name = archive_path.split("/")[-1]
    no_ext = file_name.split(".")[0]
    _path = f"/data/web_static/releases/{no_ext}"

    try:
        put(archive_path, '/tmp/')
        run(f"mkdir -p {_path}")
        run(f"tar -xzvf {file_name} -C {_path}")
        run(f"rm -f '/tmp/'{file_name}")
        run(f"mv {_path}/web_static/* {_path}")
        run(f"rm -rf {_path}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {_path} /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

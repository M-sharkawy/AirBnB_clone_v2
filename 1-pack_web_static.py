#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of
the web_static folder of the AirBnB Clone repo'''

from fabric.api import *
from datetime import datetime


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

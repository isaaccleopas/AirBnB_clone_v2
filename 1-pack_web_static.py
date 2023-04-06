#!/usr/bin/python3
"""
Fabric script to create a .tgz archive of web_static contents of web_static folder
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir

def do_pack():
    """Create a tgz archive from the contents of the web_static folder"""
    if not exists("versions"):
        local("mkdir versions")
    time_format = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_format)
    if local("tar -czvf {} web_static".format(file_path)).failed:
        return None
    return file_path

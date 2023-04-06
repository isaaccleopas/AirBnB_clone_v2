#!/usr/bin/python3
"""
Fabric script to create a .tgz archive of web_static contents
of web_static folder
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir

def do_pack():
    """Creates a compressed archive of web_static content"""
    if not isdir("versions"):
        local("mkdir versions")
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    if local("tar -czvf {} web_static".format(file_name)).failed:
        return None
    return file_name

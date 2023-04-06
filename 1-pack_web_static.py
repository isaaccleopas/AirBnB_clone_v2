#!/usr/bin/python3
"""Fabric script to create a .tgz archive of web_static contents"""

from fabric.api import local, env
from datetime import datetime

def do_pack():
    """Creates a compressed archive of web_static"""
    local("mkdir -p versions")
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H$M%S%"))
    command = "tar -cvzf {} web_static".format(archive_name)
    result = local(command)
    if result.failed:
        return None
    else:
        return archive_name

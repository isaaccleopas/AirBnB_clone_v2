#!/usr/bin/python3
"""Fabric script to create a .tgz archive of web_static contents"""

import os
from fabric.api import local
from datetime import datetime

def do_pack():
    """Creates a compressed archive of web_static"""
    if not os.path.exists("versions"):
        os.makedir("versions")
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_filename = "web_static_{}.tgz".format(timestamp)
    archive_command = "tar -czvf {0} {1}".format(
            os.path.join("versions", archive_filename),
            os.pathe.join("web_static")
    )
    result = local(archive_command)

    if result.failed:
        return None
    return os.path.join("versions", archive_filename)

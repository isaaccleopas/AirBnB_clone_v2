#!/usr/bin/python3
"""
Fabric script to distribute an archive to your web servers
using the function do_deploy.
"""

import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['54.152.246.245', '54.144.141.32']

def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    remote_path = "/tmp/{}".format(filename)
    put(archive_path, remote_path)

    foldername = filename.split(".")[0]
    path = "/data/web_static/releases/{}/".format(foldername)
    run("mkdir -p {}".format(path))
    run("tar -xzf {} -C {}".format(remote_path, path))
    run("rm {}".format(remote_path))
    run("mv {}web_static/* {}".format(path, path))
    run("rm -rf {}web_static".format(path))
    run("rm -f /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(path))

    return True

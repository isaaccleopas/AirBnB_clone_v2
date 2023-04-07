#!/usr/bin/python3
"""Fabfile to create and distribute an archive to a web server."""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.152.246.245', '54.144.141.32']


def do_pack():
    """
    Compress files and create a new archive.
    """
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """
    Distribute archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_name = os.path.basename(archive_path)
        no_ext_name = os.path.splitext(archive_name)[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_name, no_ext_name))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(no_ext_name, no_ext_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext_name))
        return True
    except:
        return False


def deploy():
    """
    Deploy web static.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

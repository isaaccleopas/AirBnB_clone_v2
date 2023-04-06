#!/usr/bin/python3
"""Fabfile to distribute an archive to a web server."""

from fabric.api import env, put, run, sudo
from os.path import exists


env.hosts = ['54.152.246.245', '54.144.141.32']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """Deploy a compressed archive to the web servers."""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_ext))
        print("New version deployed!")
        return True
    except:
        return False

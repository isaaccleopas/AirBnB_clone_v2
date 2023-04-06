#!/usr/bin/python3
"""
Fabric script for deploying web_static content to web servers
"""

from fabric.api import env, put, run
from os.path import exists, basename

env.hosts = ['54.152.246.245', '54.144.141.32']

def do_deploy(archive_path):
    """Deploy the archive to the web servers"""
    if not exists(archive_path):
        return False

    file_name = basename(archive_path).split('.')[0]

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(basename(archive_path), file_name))
        run("rm /tmp/{}".format(basename(archive_path)))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name))
        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False

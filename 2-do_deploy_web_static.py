#!/usr/bin/python3
"""Fabfile to distribute an archive to a web server."""

from fabric.api import env, put, run, sudo
from os.path import exists


env.hosts = ['54.152.246.245', '54.144.141.32']
env.user = 'ubuntu'
env.key_filename = '/home/vagrant/.ssh/id_rsa'

def do_deploy(archive_path):
    """Distributes an archive to a web server.
    """
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except:
        return False

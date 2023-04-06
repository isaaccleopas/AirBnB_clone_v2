#!/usr/bin/python3
"""Fabfile to distribute an archive to a web server."""

from fabric.api import env, put, run, sudo
from os.path import exists


env.hosts = ['54.152.246.245', '54.144.141.32']
env.user = 'ubuntu'
env.key_filename = '/home/vagrant/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1]
        foldername = '/data/web_static/releases/' + filename[:-4]
        run('sudo mkdir -p {} && sudo tar -xzf /tmp/{} -C {}'
            .format(foldername, filename, foldername))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {}/web_static/* {}/'.format(foldername, foldername))
        run('sudo rm -rf {}/web_static'.format(foldername))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(foldername))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Error: {}".format(e))
        return False

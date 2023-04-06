#!/usr/bin/python3
"""
Fabric script for deploying web_static content to web servers
"""

from fabric.api import env, put, run
from os.path import exists, basename

env.hosts = ['54.152.246.245', '54.144.141.32']
env.user = 'vagrant'
env.key_filename = '/home/vagrant/.ssh/id_rsa'

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = basename(archive_path)
        archive_noext = splitext(archive_filename)[0]
        releases_path = '/data/web_static/releases/{}'.format(archive_noext)
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, releases_path))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))

        return True

    except Exception as e:
        print(e)
        return False


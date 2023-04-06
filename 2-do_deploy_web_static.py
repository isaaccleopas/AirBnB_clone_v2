#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that distributes..
    ..an archive to your web servers, using the function do_deploy: """


from fabric.api import put, run, local, env
from os.path import exists

env.hosts = ['54.152.246.245', '54.144.141.32']

def do_deploy(archive_path):
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

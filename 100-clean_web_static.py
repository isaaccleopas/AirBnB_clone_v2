#!/usr/bin/python3
"""
This module contains a Fabric script that deletes out-of-date archives.
"""


from datetime import datetime
from fabric.api import env, run, local
import os


def do_clean(number=0):
    """
    This function deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    Returns:
        Nothing.
    """
    if int(number) < 1:
        number = 1
    else:
        number = int(number)

    local('mkdir -p versions')
    archives = local('ls -1t versions', capture=True).split('\n')
    for archive in archives[number:]:
        local('rm -rf versions/{}'.format(archive))

    run("mkdir -p /data/web_static/releases")
    archives = run("ls -1t /data/web_static/releases").split()
    for archive in archives[number:]:
        if archive != "test":
            path = "/data/web_static/releases/{}".format(archive)
            run("rm -rf {}".format(path))

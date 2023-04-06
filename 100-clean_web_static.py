#!/usr/bin/env python3
"""
This module contains a Fabric script that deletes out-of-date archives.
"""
from datetime import datetime
from fabric.api import env, run, local
import os


env.hosts = ['54.152.246.245', '54.144.141.32']


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

    for i in range(number, len(archives)):
        local('rm -rf versions/{}'.format(archives[i]))

    run("mkdir -p /data/web_static/releases")
    archives = run("ls -1t /data/web_static/releases").split()
    for i in range(number, len(archives)):
        if archives[i] != "test":
            path = "/data/web_static/releases/{}".format(archives[i])
            run("rm -rf {}".format(path))

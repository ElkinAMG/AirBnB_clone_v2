#!/usr/bin/python3
"""
Distributes an archive to your web servers.
"""

from fabric.api import put, run, env
from os.path import exists


env.hosts = [
    '35.229.108.128',
    '107.21.161.159'
]


def do_deploy(archive_path):
    "Make a deploy to a remote server.
    "

    ret = False

    if exists(archive_path):
        try:
            filename = archive_path.split('/')[-1]
            un_path = "/data/web_static/releases/{}".format(
                filename.split('.')[0]
            )

            put(archive_path, '/tmp/')

            run('mkdir -p {}'.format(un_path))

            run('tar -xzf /tmp/{} -C {}'.format(filename, un_path))
            run('rm /tmp/{}'.format(filename))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(un_path))

            ret = True
        except:
            ret = False

    return ret

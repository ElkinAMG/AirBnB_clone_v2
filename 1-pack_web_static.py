#!/usr/bin/python3
"""
Generates a .tgz archive for content in web_static.
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """
    Create a pack for web_static.
    """

    try:
        time = datetime.now()
        if not isdir("versions"):
            local("mkdir -p versions")

        _path = "web_static_{}{}{}{}{}{}.tgz".format(time.year, time.month,
                                                     time.day, time.hour,
                                                     time.minute, time.second)

        local("tar -cvzf versions/{} web_static/".format(_path))
    except:
        _path = None

    return _path

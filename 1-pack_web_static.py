#!/usr/bin/python3
"""Fabric Script that generates a .tgz archive from the contents of
the web_static folder using the function do_pack"""
import datetime
import os
from fabric.api import local
now = datetime.datetime.now()


def do_pack():
    """Generates a .tgz archive"""
    local("mkdir -p versions")
    current_time = now.strftime("%Y%m%d%H%M%S")
    tgz_file = 'web_static_' + current_time + '.tgz'
    local("tar -cvzf {} ./web_static".format(tgz_file))
    local("mv {} versions".format(tgz_file))
    fpath = local("readlink -f {}".format(tgz_file))
    return fpath

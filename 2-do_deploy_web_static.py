#!/usr/bin/python3
"""calls do_deploy to distribute the archives to the web server"""
from fabric.api import *
import os
import datetime
now = datetime.datetime.now()


env.hosts = ['35.227.97.247', '35.196.203.239']
env.user = "ubuntu"


def do_pack():
    """Generates a .tgz archive"""
    try:
        local("mkdir -p versions")
        current_time = now.strftime("%Y%m%d%H%M%S")
        tgz_file = 'web_static_' + current_time + '.tgz'
        local("tar -cvzf {} ./web_static".format(tgz_file))
        local("mv {} versions".format(tgz_file))
        fpath = "version/web_static{}.tgz".format(current_time)
        return fpath
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to te web server"""
    if not archive_path:
        return False

    rel = "/data/web_static/releases/"
    fpath = os.path.basename("{}".format(archive_path))
    dest = rel + fpath
    try:
        """upload archive to the /tmp directory"""
        put(archive_path, "/tmp/")

        """uncompress the archive to a folder /data/web_static/releases/..."""
        run("sudo mkdir -p {}{}".format(rel, fpath))
        run("sudo tar -xzf /tmp/{} -C {}".format(fpath, dest))

        """delete the archive from the web server"""
        run("sudo rm /tmp/{}".format(fpath))

        run("sudo mv {}/web_static/* {}/".format(dest, dest))
        """delete the symbolic link from web server"""
        run("sudo rm -rf {}/web_static".format(dest))
        run("sudo rm -rf /data/web_static/current")

        """create a symlink between files"""
        run("sudo ln -s {} /data/web_static/current".format(dest))

        return True

    except Exception:
        return False

#!/usr/bin/python3
from fabric.api import local, run, lcd
from datetime import datetime

def do_pack():
    # Get the current timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the archive name and path
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Compress the contents of web_static into the archive
    result = local("tar -czvf {} web_static".format(archive_path))

    # Check if the compression was successful
    if result.succeeded:
        return archive_path
    else:
        return None

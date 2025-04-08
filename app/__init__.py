import os
import shutil
from app.config import ARCHIVE_DIRECTORY
import watchdog


def process_path(path: str):
    results = []
    if "--" in path:
        unripe_name = os.path.basename(path)
        unripe_file_name, extension = os.path.splitext(unripe_name)
        file_name, filters = unripe_file_name.split("--")
        destination_path = filters.replace("-", os.path.sep)
        results = [file_name + extension, os.path.join(ARCHIVE_DIRECTORY, destination_path, file_name +extension)]
    else:
        results = [os.path.basename(path), "bad_formatting"]
    return results

def fetch_object(object: str):
    if os.path.isdir(object):
        paths = os.listdir(object)
        for item in paths:
            fetch_object(item)
    else:
        process_path(object)

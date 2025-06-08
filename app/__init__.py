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

def fetch_object(path: str):
    """Recursively process ``path`` and return a list of processed results."""

    results = []
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            results.extend(fetch_object(item_path))
    else:
        results.append(process_path(path))
    return results

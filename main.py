from app import fetch_object
from app.config import CURRENT_DIRECTORY, ARCHIVE_DIRECTORY
from watchdog.observers import Observer
from app.file_observers import FSEHandler
import time

if __name__ == "__main__":
    fetch_object(CURRENT_DIRECTORY)
    observer = Observer()
    handler = FSEHandler()
    observer.schedule(handler, path=CURRENT_DIRECTORY, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

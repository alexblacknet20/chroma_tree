from watchdog.events import DirCreatedEvent, FileCreatedEvent, FileSystemEventHandler


class FSEHandler(FileSystemEventHandler):
    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        print(f"file {event.src_path} are created")

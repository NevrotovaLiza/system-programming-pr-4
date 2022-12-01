import time
from watchdog.observers import Observer
from shedule_class import FileShedule

event_handler = FileShedule()
observer = Observer()
path = f"./files"
observer.schedule(event_handler, path=path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
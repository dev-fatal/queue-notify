from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
from message import send_message
import os


class ScanFolder:
    def __init__(self, path, token, chat_id):
        self.path = path + "\\_retail_\\Screenshots"
        self.token = token
        self.chat_id = chat_id
        self.event_handler = PatternMatchingEventHandler(patterns=["*.tga"], ignore_patterns=None,
                                                         ignore_directories=False, case_sensitive=True)
        self.event_handler.on_created = self.on_created
        self.observer = Observer()
        self.observer.schedule(self.event_handler, self.path, recursive=False)
        self.observer.start()

    def on_created(self, event):
        send_message(self.token, self.chat_id)
        print("Sending message...")
        if os.path.exists(event.src_path):
            os.remove(event.src_path)

    def stop(self):
        self.observer.stop()
        self.observer.join()


def monitor(path, token, chat_id):
    observer = ScanFolder(path, token, chat_id)
    print("Monitoring...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

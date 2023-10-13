import threading

class Consumer(threading.Thread):
    def __init__(self, name, buffer):
        threading.Thread.__init__(self)
        self.name = name
        self.buffer = buffer

    def run(self):
        message = self.buffer.get()
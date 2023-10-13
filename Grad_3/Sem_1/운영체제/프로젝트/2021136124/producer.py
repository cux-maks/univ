import threading
import random

class Producer(threading.Thread):
    def __init__(self, name, buffer):
        threading.Thread.__init__(self)
        self.name = name
        self.buffer = buffer

    def run(self):
        message = random.randrange(1, 101)
        self.buffer.put(message)
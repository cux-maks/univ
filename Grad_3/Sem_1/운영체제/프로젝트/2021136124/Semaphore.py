import threading

class Semaphore:
    def __init__(self, initial_value):
        self.value = initial_value
        self.mutex = threading.Lock()
        self.queue = []
        self.condition = threading.Condition(self.mutex)

    def P(self):
        with self.mutex:
            if self.value > 0:
                self.value -= 1
            else:
                self.queue.append(threading.current_thread())
                self.condition.wait()

    def V(self):
        with self.mutex:
            if self.queue:
                thread = self.queue.pop(0)
                self.condition.notify()
            else:
                self.value += 1
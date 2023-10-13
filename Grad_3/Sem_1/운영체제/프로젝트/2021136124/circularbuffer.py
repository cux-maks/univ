from Semaphore import Semaphore
import time

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None for _ in range(size)]
        self.in_index = 0
        self.out_index = 0
        self.nrfull = Semaphore(0)
        self.nrempty = Semaphore(size)
        self.mutexP = Semaphore(1)
        self.mutexC = Semaphore(1)

    def put(self, message):
        self.nrempty.P()
        self.mutexP.P()
        time.sleep(3)
        self.buffer[self.in_index] = message
        self.in_index = (self.in_index + 1) % self.size
        self.nrfull.V()
        self.mutexP.V()

    def get(self):
        self.nrfull.P()
        self.mutexC.P()
        message = self.buffer[self.out_index]
        time.sleep(3)
        self.buffer[self.out_index] = None
        self.out_index = (self.out_index + 1) % self.size
        self.nrempty.V()
        self.mutexC.V()
        return message

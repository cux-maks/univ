import threading
import time


class Counter:
  def __init__(self, initial_value = 0):
    self.value = initial_value
    self.value_lock = threading.Lock()
    self._start()
  
  def incr(self,delta=1):
    self.value_lock.acquire()
    for i in range(100000):
      self.value += delta
    self.value_lock.release()
  
  def decr(self,delta=1):
    self.value_lock.acquire()
    for i in range(100000):
      self.value -= delta
    self.value_lock.release()
  
  def _start(self):
    t1 = threading.Thread(target=self.incr, args=(1,))
    t2 = threading.Thread(target=self.decr, args=(1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

counter = Counter()
counter.value
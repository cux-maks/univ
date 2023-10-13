# Quiz Blcok
from queue import Queue
from threading import Thread
from threading import Event
import numpy as np

_sentinel = object()
data = [(1, 1), ]

def update_data(data_):
  global data
  data.append((data_[0] + 1, data_[0] + 1))
  if not (data[0] == (5, 5) and len(data) >= 2):
    print((data_[0] + 1, data_[0] + 1))
    print(data)

def producer(out_q):
  global data
  while True:
    out_q.put(data[0])
    if data[0] == (5, 5): break
    del data[0]
    out_q.join()

  out_q.put(_sentinel)

def consumer(in_q):
  while True:
    data = in_q.get()
    if data is _sentinel:
      in_q.put(_sentinel)
      break
    update_data(data)
    in_q.task_done()

q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
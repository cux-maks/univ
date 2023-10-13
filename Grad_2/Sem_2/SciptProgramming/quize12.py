import threading
import time

class CounterThread(threading.Thread):
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()
 
    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()
    
    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()
    
    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()
 
if __name__ == '__main__':
    totalCount = 0

    timerThread = CounterThread(0)
    timerThread.start()

    def count(n):
        global totalCount
        while n > 0:
            # print(n)
            timerThread.wait_for_tick()
            totalCount += 1
            n -= 1
    
    threads = []
    for _ in range(4):
        buf = threading.Thread(target=count, args=(250000, ))
        threads.append(buf)
        buf.start()
    
    for th in threads:
        th.join()
 
    print('totalCount = ' + str(totalCount))
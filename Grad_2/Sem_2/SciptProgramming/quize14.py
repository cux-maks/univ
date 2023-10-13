import numpy as np
from multiprocessing import Pool
import time
 
arr = np.random.random(1000000)

def mul(x):
  return x * 10

p = Pool(4)
start = time.time()
# result = [mul(x) for x in arr]
arr = p.apply(mul, (arr, ))
end = time.time()
p.close()
p.join()
print("{0:1.3f}".format(end - start))
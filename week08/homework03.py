
import functools
import time

def timer(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        print('%s 运行了 %f 秒' % (fn.__name__, time.time() - start))
        return result

    return wrapper
   
@timer
def test(n):
    time.sleep(n)
    print("运行结束了")

test(3)
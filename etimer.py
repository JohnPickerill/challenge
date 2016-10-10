import time
          
def exec_timer(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.clock()
        result = func(*args, **kwargs)
        # use clock rather than time for higher resolution
        end_ts = time.clock()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return result
    return wrapper
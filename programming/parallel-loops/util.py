# util.py

from functools import wraps
import time

# cpu time measuring decorator
def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        # get the start time
        st = time.process_time()
        value = func(*args, **kwargs)
        # get the end time
        et = time.process_time()
        # get execution time
        res = et - st
        print(f'CPU Execution time: {res:0.8f}', 'seconds')
    return wrapper_timer

# execute a task
def task(value):
    quot = value%2
    print(f'.done {value} || {quot}', flush=True)
    return quot
# superfastpython.com
# example of parallel for loop with the Thread class
from util import task, timer

@timer
def impl_thread(no_of_threads):
    from threading import Thread

    # create all tasks
    threads = [Thread(target=task, args=(i,)) for i in range(no_of_threads)]
    # start all threads
    for thread in threads:
        thread.start()
    # wait for all threads to complete
    for thread in threads:
        thread.join()
    # report that all tasks are completed
    print('Done')

@timer
def impl_threadpool(no_of_threads):
    from multiprocessing.pool import ThreadPool

    with ThreadPool() as pool:
        # issue one task with the default number of workers
        for result in pool.map(task, range(no_of_threads)):
            # handle the result
            print(f'> got {result}')
        # report that are all tasks are completed
        print('Done')


if __name__ == '__main__':

    no_of_threads = 1000

    # call the Thread implementation
    # impl_thread(no_of_threads)

    # call the ThreadPool implementation
    impl_threadpool(no_of_threads)




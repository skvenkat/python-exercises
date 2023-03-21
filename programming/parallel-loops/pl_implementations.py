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
def impl_threadpool(no_of_tasks):
    from multiprocessing.pool import ThreadPool

    with ThreadPool() as pool:
        # issue one task with the default number of workers
        for result in pool.map(task, range(no_of_tasks)):
            # handle the result
            #print(f'> got {result}')
            pass
        # report that are all tasks are completed
        print('Done')

@timer
def impl_threadpoolexecutor(no_of_tasks):
    import concurrent.futures

    # create the pool with default number of workers
    with  concurrent.futures.ThreadPoolExecutor() as tpexec:
        # issue some tasks and collect futures
        futures = [tpexec.submit(task, i) for i in range(no_of_tasks)]
        # handle results as tasks are completed
        for future in concurrent.future.as_completed(futures):
            #print(f'> got {future.result}')
            pass
        # issue one task for each call to the function
        for result in tpexec.map(task, range(no_of_tasks)):
            #print(f'> got {result}')
            pass
        #report that are all tasks are completed
        print('Done')

@timer
def impl_processclass(no_of_processes):
    from multiprocessing import Process
    # create all tasks
    processes = [Process(target=task, args=(i,)) for i in range(no_of_processes)]
    # start all processes
    for proc in processes:
        proc.start()
    # wait for all processes to complete
    for process in processes:
        process.join()
    # report that all tasks are completed
    print('Done')

@timer
def impl_poolclass(no_of_tasks):
    from multiprocessing import pool

    # create a pool with deafult number of workers
    with Pool() as pool:
        # issue one task for each call to the function
        for result in pool.map(task, range(no_of_tasks)):
            # handle the result
            #print(f'> got {result}')
            pass
    # report that all tasks are completed
    print('Done')

@timer
def impl_processpoolexecutor(no_of_tasks):
    import concurrent.futures

    with concurrent.futures.ProcessPoolExecutor() as ppexec:
        # issue some tasks and collect futures
        futures = [ppexec.submit(task, i) for i in range(no_of_tasks)]
        # process results as tasks are completed
        for future in concurrent.futures.as_completed(futures):
            #print(f'> got {future.result}')
            pass
        # issue one task for each call to the function
        for result in ppexec.map(task, no_of_tasks):
            #print(f'> got {result}')
            pass
    # report that all tasks are completed
    print('Done')

if __name__ == '__main__':

    no_of_threads, no_of_tasks = 100, 100

    # call the Thread implementation
    impl_thread(no_of_threads)

    # call the ThreadPool implementation
    impl_threadpool(no_of_tasks)

    # call the ThreadPoolExecutor implmentation
    impl_processpoolexecutor(no_of_tasks)

    # call the Process implmentation
    impl_processclass(no_of_tasks)

    # call the Pool Implementation
    impl_poolclass(no_of_tasks)

    # call the ProcessPoolExecutor implementation
    impl_processpoolexecutor(no_of_tasks)


